import requests

params = {
    "q" : "agentic",
    "sort": "stars",
    "order": "desc",
    "per_page": 10
}

response = requests.get("https://api.github.com/search/repositories", params=params)

data = response.json()

if response.status_code == 200:
    items = data["items"]

    for i in items:
        print(i["full_name"])

