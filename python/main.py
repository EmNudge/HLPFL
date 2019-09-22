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
        # print()
        # print()
        # print()
        # print()
        # print()
        # print("########## ARTICLE ##########")
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


# info = {
#     "event": "hurricane hermine",
#     "location": "united states",
#     "date": "2016-09-22"
# }

# info = {
#     "event": "lombok earthquake",
#     "location": "indonesia",
#     "date": "2018-08-12"
# }

{"event": "lombok earthquake","location": "indonesia","date": "2018-08-12"}