import json
from fuzzywuzzy import fuzz
from google.cloud import language_v1
from google.cloud.language_v1 import enums

def _parse(article, data):
    for key, value in data.items():
        if isinstance(value, str):
            data[key] = value.lower()
    for key, value in article.items():
        if isinstance(value, str):
            article[key] = value.lower()
        

def analyze(article, data):
    """
    Analyzing Entities in a String

    Args:
      data["article"]: The text content to analyze
    """

    # ASSUMED INPUT
    # data["disaster"], data["location"], data["date"], data["reports"]

    # ASSUMED ARTICLE
    # article["text"], article["url"]

    # const
    valid_categories = [
        "/Law & Government/Public Safety",
        "/Law & Government",
        "/Law & Government/Public Safety/Emergency Services",
        "/News",
        "/News/Weather",
        "/News/Health News",
        "/Science/Ecology & Environment/Climate Change & Global Warming",
        "/Sensitive Subjects"
    ]

    valid_disasters = [
        "hurricane",
        "typhoon",
        "earthquake",
        "tornado",
        "monsoon",
        "flood",
        "tsunami",
        "drought",
        "famine"
    ]

    annotations = "damage hurricane storm death toll rain flood dead casualty fatal hurricane damage waves sea danger warning"
    year, month, day = [int(a) for a in data["date"].split("-")]

    # Init API client
    client = language_v1.LanguageServiceClient()

    # vars
    valid_location = False
    valid_date = False
    valid_event = False
    valid_category = False
    valid_score = False

    confidence = 0
    hits = 0
    score = 0
    sal = 0

    # Settings
    type_ = enums.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": article["article"], "type": type_, "language": language}
    encoding_type = enums.EncodingType.UTF8

    # Get entity responses
    entity_response = client.analyze_entities(document, encoding_type=encoding_type)
    for entity in entity_response.entities:
        _type = enums.Entity.Type(entity.type).name

        # print(u"Entity Name: {}".format(entity.name))
        # print(u"Entity type: {}".format(_type))
        # print(u"Salience score: {}".format(entity.salience))

        if _type == "LOCATION":
            fz_score = fuzz.partial_ratio(entity.name.lower(), data["location"])
            # print(u"mentions: {}".format(len(entity.mentions)))        
            # print(u"fuzz score: {}".format(fz_score))
            if fz_score > 70:
                # print('------------- HIT -----------------')
                hits += 1
                sal += entity.salience * 0.5
                valid_location = True
            # for mention in entity.mentions:
            #     print(u"Mention text: {}".format(mention.text.content))
            #     print(u"Mention type: {}".format(enums.EntityMention.Type(mention.type).name))
        elif _type == "EVENT":
            fz_score = fuzz.partial_ratio(entity.name.lower(), data["disaster"])
            # print("events")
            # print(u"fuzz score: {}".format(fz_score))
            if fz_score > 70:
                # print('------------- HIT -----------------')
                hits += 1
                sal += entity.salience
                valid_event = True
            elif (fuzz.partial_ratio(entity.name.lower(), annotations) > 70):
                hits += 1
                sal += entity.salience
        elif _type == "DATE":
            # print("date")
            if (entity.metadata["month"] and entity.metadata["year"]):
                if (month == 1 and int(entity.metadata["month"]) == 1 and (year == int(entity.metadata["year"]) or year == int(entity.metadata["year"])-1)):
                    valid_date=True
                elif (month == int(entity.metadata["month"]) or month == int(entity.metadata["month"])-1):
                    valid_date=True
        else:
            fz_score = fuzz.partial_ratio(entity.name.lower(), annotations)
            # print("defualt")
            # print(u"fuzz score: {}".format(fz_score))
            if fz_score > 80:
                # print('------------- HIT -----------------')
                hits += 1
                sal += entity.salience * 0.75
        # print()
        
    category_response = client.classify_text(document)
    for category in category_response.categories:
        # print(u"Category name: {}".format(category.name))
        # print(u"Confidence: {}".format(category.confidence))
        if category.name in valid_categories and category.confidence > 0.5:
            # print('------------- category HIT -----------------')
            valid_category = True
            confidence += 1
    
    # Caluclate score
    score += confidence / len(category_response.categories)
    score += min(hits/len(data["article"].split(" ")), 0.10) * 10
    score += min(sal, 1.0)
    score /= 3

    valid_score = score > 0.25

    print(score, valid_category, valid_location, valid_date, valid_event, valid_score)

if __name__ == "__main__":
    with open("articles.json", 'r') as fi:
        data = json.load(fi)
    for i,dat in enumerate(data):
        analyze(dat,dat)