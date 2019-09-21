from fuzzywuzzy import fuzz

from google.cloud import language_v1
from google.cloud.language_v1 import enums


def _parse_input(annotations):
    annotations["di"]

    real_disaster = real_disaster.lower()
    real_location = real_location.lower()
    real_date = real_date.split("-")
    return real_disaster, real_location, real_date, real_reports

def _parse_articles(annotations):
    pass


def _analyze(article, real_disaster, real_location, real_date, real_reports):
    """
    Analyzing Entities in a String

    Args:
      article: The text content to analyze
    """

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

    # Init API client
    client = language_v1.LanguageServiceClient()
    hits = 0
    score = 0
    sal = 0

    # Settings
    type_ = enums.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": article, "type": type_, "language": language}
    encoding_type = enums.EncodingType.UTF8

    # Get entity responses
    entity_response = client.analyze_entities(document, encoding_type=encoding_type)
    for entity in entity_response.entities:
        print(u"Entity Name: {}".format(entity.name))
        print(u"Entity type: {}".format(enums.Entity.Type(entity.type).name))
        print(u"Salience score: {}".format(entity.salience))


        if enums.Entity.Type(entity.type).name == "LOCATION":
            fz_score = fuzz.partial_ratio(entity.name.lower(), real_disaster.lower())
            print(u"mentions: {}".format(len(entity.mentions)))        
            print(u"fuzz score: {}".format(fz_score))
            if fz_score > 60:
                print('------------- category HIT -----------------')
                hits += 1
                sal += entity.salience
            # for mention in entity.mentions:
            #     print(u"Mention text: {}".format(mention.text.content))
            #     print(u"Mention type: {}".format(enums.EntityMention.Type(mention.type).name))

        if enums.Entity.Type(entity.type).name == "EVENT":
            fz_score = fuzz.partial_ratio(entity.name.lower(), real_disaster.lower())
            print("events")
            print(u"fuzz score: {}".format(fz_score))
            if fz_score > 60:
                print('------------- category HIT -----------------')
                hits += 1
                sal += entity.salience

        # if enums.Entity.Type(entity.type).name == "DATE":
        #     print("date")
        #     for key, value in entity.metadata.items():
        #         if value in real_date
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

    score += min(hits/len(article.split(" ")), 0.10) * 10
    score += min(sal, 1.0)
    score /= 2

    print(hits, hits/len(article.split(" ")), sal, score)

    return score > 0.2

if __name__ == "__main__":
    article = """
    Puerto Rico revises Hurricane Maria death toll 01:39
    (CNN)Puerto Rico's new death toll from Hurricane Maria is making the storm one of the deadliest hurricanes in US history.

    Authorities raised the death toll from last year's storm to 2,975 on Tuesday, which surpasses that of both Hurricane Katrina in 2005, which is responsible for 1,833 deaths, and the 1928 Okeechobee hurricane in Florida, which killed 2,500 people.
    The count in Puerto Rico could change as the government continues to investigate deaths from the storm, Puerto Rico Gov. Ricardo Roselló said. Until the recent update, Puerto Rico's government had said only 64 people died as a result of the storm.
    Puerto Rico&#39;s new Hurricane Maria death toll is 46 times higher than the government&#39;s previous count
    Puerto Rico's new Hurricane Maria death toll is 46 times higher than the government's previous count
    The Great Galveston Hurricane of 1900 remains the deadliest recorded hurricane in US history.
    Thousands of homes in the city of Galveston, Texas were reduced to rubble by a hurricane on Sept. 8, 1900. 
    Thousands of homes in the city of Galveston, Texas were reduced to rubble by a hurricane on Sept. 8, 1900.
    When it made landfall on September 8, 1900, it destroyed thousands of homes and killed at least 8,000 people within hours. The hurricane hit the Texas port city by surprise and had such a massive impact that it "brought a new focus on the study of hurricane prediction," the National Oceanic and Atmospheric Administration said.
    All three of the deadliest hurricanes were Category 4 storms when they made landfall.
    Deadly estimates in the spotlight
    News organizations and some members of Congress have raised questions about the official death toll in Puerto Rico, which had remained at 64 for months.
    CNN reporters surveyed about half of the funeral homes across the island and found that funeral home directors identified 499 deaths they considered to be hurricane-related. In December, The New York Times estimated 1,052 "excess deaths" occurred after Maria. Others produced similar estimates.
    Democrats in the House, including some Hispanic Caucus members, have requested an investigation into the Trump administration's response to Hurricane Maria.
    In June, Democratic Rep. Nydia Velázquez called for a commission similar to one established in the aftermath of 9/11 to look into the storm's "death toll, the federal response and how FEMA and other agencies may have responded sluggishly based on artificially low numbers."
    CNN's Leyla Santiago, Catherine E. Shoichet and Jason Kravarik contributed to this report.
    """

    real_disaster = "hurricane storm typhoon death toll "
    real_location = "puerto rico"
    real_date = "2018"
    real_reports = 5

    _analyze(article, real_disaster, real_location, real_date, real_reports)