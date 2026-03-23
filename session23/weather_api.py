import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("NEWS_KEY")


url = f"https://newsdata.io/api/1/latest?apikey={API_KEY}&q=nepal"

response = requests.get(url)
data = response.json()
print(data["totalResults"])