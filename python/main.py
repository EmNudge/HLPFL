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

        if _type == "LOCATION":
            fz_score = fuzz.partial_ratio(entity.name.lower(), data["location"])
            if fz_score > 60:
                hits += 1
                sal += entity.salience * 0.5
                valid_location = True
        elif _type == "EVENT":
            fz_score = fuzz.partial_ratio(entity.name.lower(), data["disaster"])
            if fz_score > 60:
                hits += 1
                sal += entity.salience
                valid_event = True
            elif (fuzz.partial_ratio(entity.name.lower(), annotations) > 60):
                hits += 1
                sal += entity.salience
        elif _type == "DATE":
            if (entity.metadata["month"] and entity.metadata["year"]):
                if (month == 1 and int(entity.metadata["month"]) == 1 and (year == int(entity.metadata["year"]) or year == int(entity.metadata["year"])-1)):
                    valid_date=True
                elif (month == int(entity.metadata["month"]) or month == int(entity.metadata["month"])-1):
                    valid_date=True
        else:
            fz_score = fuzz.partial_ratio(entity.name.lower(), annotations)
            if fz_score > 80:
                hits += 1
                sal += entity.salience * 0.75
    
    category_response = client.classify_text(document)
    for category in category_response.categories:
        if category.name in valid_categories and category.confidence > 0.5:
            valid_category = True
            confidence += 1
    
    # Caluclate score
    score += confidence / len(category_response.categories)
    score += min(hits/len(data["article"].split(" ")), 0.10) * 10
    score += min(sal, 1.0)
    score /= 3

    valid_score = score > 0.25

    print(score, valid_category, valid_location, valid_date, valid_event, valid_score)
    return valid_score and valid_category and valid_location and valid_date and valid_event, score

if __name__ == "__main__":
    with open("articles.json", 'r') as fi:
        data = json.load(fi)
    for i,dat in enumerate(data):
        analyze(dat,dat)