
import requests

URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(URL)

data = json.loads(response.content.decode("utf-8"))

data