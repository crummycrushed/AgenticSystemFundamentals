import requests

url = "https://covid-19-data.p.rapidapi.com/country/code"

querystring = {"format":"json","code":"it"}

headers = {
	"x-rapidapi-host": "covid-19-data.p.rapidapi.com",
	"Content-Type": "application/json"
}

for i in range(20):
    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 429:
        print("Rate limit exceeded. Please wait and retry")