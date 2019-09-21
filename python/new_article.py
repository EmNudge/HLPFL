import json

new_dat = {
    "location": "puerto rico",
    "disaster": "hurricane",
    "date": "2017-09-19",
    "annotations": "maria",
    "reports": -1,
    "article": """
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
}

with open("articles.json", 'r') as fi:
    data = json.load(fi)
    data.append(new_dat)

with open("articles.json", 'w') as fo:
    json.dump(data, fo, indent=2)