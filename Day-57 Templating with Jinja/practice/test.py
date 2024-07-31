import requests

API_KEY = "db1e74f605ee00a539bd00af7e7f52aa"
web = f"https://api.genderize.io?name=peter"


response = requests.get(url=web)

data = response.json()

print(data)