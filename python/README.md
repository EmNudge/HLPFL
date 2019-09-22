# NLP Disaster Verification 
---
Confirms a natural disaster event by scraping rwlabs disaster API and score it using GCloud NLP API and fuzzy searching.

## Use
```python
import requests
import json

url = "https://hackathons-1569045593351.appspot.com/entry"
data = json.dumps({
    "event": "hurricane hermine",
    "location": "united states",
    "date": "2016-09-22"
})

response = requests.post(url, data=data)
print(json.dumps(response.json(), indent=2))
```
```
{
  'date':'2016-09-22',
  'event':'hurricane hermine',
  'location':'united states',
  'summary':'UN says Hurricane Hermine is wake up call for an active hurricane season',
  'url':'https://reliefweb.int/report/united-states-america/un-says-hurricane-hermine-wake-call-active-hurricane-season'
}
```
