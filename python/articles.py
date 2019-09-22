import requests
import json

def get_articles(event):
    url = f"https://api.reliefweb.int/v1/reports?appname=apidoc&query[value]={event}"
    response = requests.request("GET", url)
    articles = response.json()["data"]
    links = [article["href"] for article in articles]

    data = []
    for link in links:
        try:
            data.append(get_article_data(link))
        except KeyError:
            pass
        print(data[-1])

    return data

def get_article_data(url):
    response = requests.request("GET", url)
    data = response.json()["data"][0]["fields"]

    return {
        "publisher": data["source"][0]["longname"],
        "homepage": data["source"][0]["homepage"],
        "date": data["date"]["original"].split("T")[0],
        "country": data["primary_country"]["name"],
        "event": data["disaster_type"][0]["name"],
        "lang": data["language"][0]["code"],
        "url": data["url_alias"],
        "title": data["title"],
        "body": data["body"]
    }

if __name__=="__main__":
    data = get_articles("hurricanes")
    print(data)