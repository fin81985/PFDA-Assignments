# Bank holidays in the northern Ireland
# Author: Finian Doonan

import requests # https://requests.readthedocs.io/en/latest/

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json() # downloads bank holiday data in JSON format

year = 2026 # specify year


# northern ireland bank holidays
for event in data["northern-ireland"]["events"]:
    if event['date'].startswith(str(year)):# check for specified year
        
        print(f"{event['title']} on {event['date']}")# prints bank holidays for the specified year


