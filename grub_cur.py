import json
import requests
url = 'https://www.cryptonator.com/api/currencies'
response = requests.get(url)

fixture = []
for rows in response.json()['rows']:
    fixture_object = {
      "model": "currencies.currency",
      "fields": {
        "name": rows['name'],
        "code": rows['code']
      }
    }
    fixture.append(fixture_object)
print(json.dumps(fixture))
