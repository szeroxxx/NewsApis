from flask import Flask, jsonify
from flask_cors import CORS
from pygnews import fetcher

app = Flask(__name__)
CORS(app)

news_fetcher = fetcher.PyGNews()

@app.route('/news', methods=['GET'])
def get_news():
    try:
        news_data = news_fetcher.location_headlines()
        return jsonify(news_data) 
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)


