import requests
import json

response = requests.get("https://api.github.com/invalid")


if response.status_code == 200:
    print("Success")
else:
    print("Failed")

