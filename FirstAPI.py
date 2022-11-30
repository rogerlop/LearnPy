import requests
import json

URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(URL)

#print(response.json())



data = json.loads(response.content.decode("utf-8"))

print(data)
