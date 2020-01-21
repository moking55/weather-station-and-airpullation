import requests

api_url = "https://api.airvisual.com/v2/nearest_city"

params = {
    'key': 'acd8e3f4-e77d-418a-9985-896cff59571e', # Token ความปลอดภัยของ API
    }
res = requests.get(api_url, params=params)


payload = {}
headers= {}

response = requests.request("GET", api_url, headers=headers, data = payload)

print(res.text.encode('UTF-8'))