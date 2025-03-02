from flask import Flask, request, jsonify
from flask_cors import CORS
from ytmusicapi import YTMusic
import os


print("Starting server...")
app = Flask(__name__)
CORS(app, origins=["https://wais-nation.vercel.app", "http://localhost:3000"])

ytmusic = YTMusic()

# Simple cache to reduce API requests
search_cache = {}

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        print("Missing query parameter")
        return jsonify({"error": "Missing query parameter"}), 400

    # ✅ Check cache first
    if query in search_cache:
        return jsonify(search_cache[query])

    # ✅ Fetch song details
    results = ytmusic.search(query, filter="songs")
    
    if results:
        first_result = results[0]
        song_data = {
            "videoId": first_result["videoId"],
            "title": first_result["title"],
            "artist": first_result["artists"][0]["name"] if first_result.get("artists") else "Unknown Artist",
            "duration": first_result["duration"],
            "thumbnail": first_result["thumbnails"][-1]["url"] if first_result.get("thumbnails") else None
        }

        # ✅ Save to cache
        search_cache[query] = song_data
        return jsonify(song_data)

    return jsonify({"error": "No results found"}), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
