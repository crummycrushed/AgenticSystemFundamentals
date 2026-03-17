import requests


# GET request is used to fetch information from the server without modifying data
response = requests.get("https://api.github.com")

#print(response.text)  #text = print raw response
print(response.status_code) #status_code = success / failure
print(type(response))

data = response.json()
print(type(data))

print(data["current_user_url"])
