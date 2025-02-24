from flask import Flask, request, jsonify
from flask_cors import CORS
from ytmusicapi import YTMusic

app = Flask(__name__)
CORS(app)
ytmusic = YTMusic()

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Missing query parameter"}), 400

    results = ytmusic.search(query, filter="songs")
    if results:
        return jsonify({"videoId": results[0]['videoId']})

    return jsonify({"videoId": None})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
