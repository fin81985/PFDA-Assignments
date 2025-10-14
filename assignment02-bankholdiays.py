# Bank holidays in the northern Ireland
# Author: Finian Doonan

import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
print (data)


# northern ireland bank holidays
for event in data["northern-ireland"]["events"]:
    #print (f"{event}")
    print (f"{event['title']} on {event['date']}")


