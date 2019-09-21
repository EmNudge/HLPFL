from fuzzywuzzy import fuzz

from google.cloud import language_v1
from google.cloud.language_v1 import enums


# def _parse_input(annotations):
#     annotations["di"]

#     real_disaster = real_disaster.lower()
#     annotations["location"] = annotations["location"].lower()
#     annotations["date"] = annotations["date"].split("-")
#     return real_disaster, annotations["location"], annotations["date"], annotations["reports"]

# def _parse_annotations["article"]s(annotations):
#     pass


def _analyze(annotations):
    """
    Analyzing Entities in a String

    Args:
      annotations["article"]: The text content to analyze
    """

    # ASSUMED INPUT
    # annotations["article"], annotations["disaster"], annotations["location"], annotations["date"], annotations["reports"], annotations["url"]

    # Const
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

    year, month, day = [int(a) for a in annotations["date"].split("-")]

    # Init API client
    client = language_v1.LanguageServiceClient()

    # vars
    valid_location = False
    valid_date = False
    valid_event = False

    hits = 0
    score = 0
    sal = 0

    # Settings
    type_ = enums.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": annotations["article"], "type": type_, "language": language}
    encoding_type = enums.EncodingType.UTF8

    # Get entity responses
    entity_response = client.analyze_entities(document, encoding_type=encoding_type)
    for entity in entity_response.entities:
        print(u"Entity Name: {}".format(entity.name))
        print(u"Entity type: {}".format(enums.Entity.Type(entity.type).name))
        print(u"Salience score: {}".format(entity.salience))


        if enums.Entity.Type(entity.type).name == "LOCATION":
            fz_score = fuzz.partial_ratio(entity.name.lower(), annotations["disaster"].lower())
            print(u"mentions: {}".format(len(entity.mentions)))        
            print(u"fuzz score: {}".format(fz_score))
            if fz_score > 65:
                print('------------- category HIT -----------------')
                hits += 1
                sal += entity.salience
                valid_location = True
            # for mention in entity.mentions:
            #     print(u"Mention text: {}".format(mention.text.content))
            #     print(u"Mention type: {}".format(enums.EntityMention.Type(mention.type).name))

        if enums.Entity.Type(entity.type).name == "EVENT":
            fz_score = fuzz.partial_ratio(entity.name.lower(), annotations["disaster"].lower())
            print("events")
            print(u"fuzz score: {}".format(fz_score))
            if fz_score > 60:
                print('------------- category HIT -----------------')
                hits += 1
                sal += entity.salience

        # if enums.Entity.Type(entity.type).name == "DATE":
        #     print("date")
        #     for key, value in entity.metadata.items():
        #         if value in annotations["date"]
        #         print(key, value, sep=":\t")

        print()
        print()
    
    print("\n"*4)

    category_response = client.classify_text(document)
    for category in category_response.categories:
        print(u"Category name: {}".format(category.name))
        print(u"Confidence: {}".format(category.confidence))
        if category.name in valid_categories and category.confidence > 0.25:
            hits += 1
            print('------------- category HIT -----------------')
        else:
            print('------------- category MISS -----------------')
            
    print("\n"*4)

    score += min(hits/len(annotations["article"].split(" ")), 0.10) * 10
    score += min(sal, 1.0)
    score /= 2

    print(hits, hits/len(annotations["article"].split(" ")), sal, score)

    return score > 0.2

if __name__ == "__main__":
    with open("annotations["article"]s.json", 'r') as fi:
        data = json.load(fi)
    

    _analyze(annotations["article"], annotations["disaster"], annotations["location"], annotations["date"], annotations["reports"])