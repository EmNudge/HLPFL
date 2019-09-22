import json
from flask import Flask, request, jsonify
from nlp import analyze
from articles import get_articles

app = Flask(__name__)

@app.route("/entry", methods=['POST'])
def entry():
    info = json.loads(request.get_data().decode('utf-8'))
    print(info)

    response = {}
    high = -1
    articles = get_articles(info["event"])
    for article in articles:
        # print("\n"*4, "########## ARTICLE ##########")
        score, valid = analyze(info, article)
        if valid and score > high:
            response = {
                "event": info["event"],
                "location": info["location"],
                "summary": article["title"],
                "url": article["url"],
                "date": info["date"]
            }

    print(response)
    return jsonify(response)
