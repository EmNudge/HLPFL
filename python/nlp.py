import json
from fuzzywuzzy.fuzz import partial_ratio as pratio
from google.cloud import language_v1
from google.cloud.language_v1 import enums

def analyze(info, article):
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
        "famine",
        "tropical cyclone",
        "cyclone"
    ]
    annotations = "damage hurricane storm death toll rain flood dead casualty fatal hurricane damage waves sea danger warning havoc wind emergency"

    # Init API client
    client = language_v1.LanguageServiceClient()

    # print("---------- title ----------")
    # print(article["title"])
    # print()
    # print("---------- body ----------")
    # print(article["body"])

    # vars
    valid_country = pratio(info["location"], article["country"]) > 75
    valid_event = pratio(info["event"], article["event"]) > 75 or max([pratio(info["event"].lower(), vd) for vd in valid_disasters]) > 0.75
    valid_date = info["date"].split("-")[:2] == article["date"].split("-")[:2]
    #  print()
    # print("---------- analysis ---------")
    # print("country:\t", info["location"], "   |||   ", article["country"], pratio(info["location"], article["country"]))
    # print("event:\t", info["event"], "   |||   ", article["event"], pratio(info["event"], article["event"]), "   |||   ", max([pratio(info["event"].lower(), vd) for vd in valid_disasters]) > 0.75)
    # print("date:\t", info["date"], "   |||   ", article["date"], "   |||   ", info["date"].split("-")[:2] == article["date"].split("-")[:2])

    # settings
    type_ = enums.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": article["title"] + ". " + article["body"], "type": type_, "language": language}
    encoding_type = enums.EncodingType.UTF8


    # print()
    # print("---------- hits ----------")
    
    # entity responses
    valid_score = False
    hits = 0
    score = 0
    entity_response = client.analyze_entities(document, encoding_type=encoding_type)
    for entity in entity_response.entities:
        _type = enums.Entity.Type(entity.type).name

        if _type == "LOCATION":
            fz_score = pratio(entity.name.lower(), article["country"])
            if fz_score > 60:
                hits += 1
                score += entity.salience * 0.5
                # print("LOCATION:\t", entity.name, entity.salience*0.5)
        elif _type == "EVENT":
            fz_score = pratio(entity.name.lower(), article["event"])
            if fz_score > 60:
                hits += 1
                score += entity.salience
                # print("EVENT:\t", entity.name, entity.salience)
            elif (pratio(entity.name.lower(), annotations) > 60):
                hits += 1
                score += entity.salience
                # print("EVENT_ANNON:\t", entity.name, entity.salience)
        else:
            fz_score = pratio(entity.name.lower(), annotations)
            if fz_score > 80:
                hits += 1
                score += entity.salience * 0.75
                # print("ANNOTATION:\t", entity.name, entity.salience*0.75)

    # print()
    # print("---------- categories ----------")
    # category responses
    valid_category = False
    confidence = 0
    category_response = client.classify_text(document)
    for category in category_response.categories:
        # print(category.name, category.confidence, category.confidence > 0.5)
        if category.name in valid_categories and category.confidence > 0.5:
            valid_category = True
            confidence += 1
    
    # Caluclate score
    score += min(score, 1.0)
    score += confidence / len(category_response.categories) if len(category_response.categories) else 0
    score += min(hits/len((article["title"] + ". " + article["body"]).split(" ")), 0.10) * 10
    score /= 3

    valid_score = score > 0.25

    # print()
    # print("---------- result ----------")
    # print(score, valid_country, valid_event, valid_date, valid_score, valid_category)

    return score, valid_country and valid_event and valid_score and valid_category
