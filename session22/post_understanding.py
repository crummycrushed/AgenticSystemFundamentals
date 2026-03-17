import requests


body = {
    "name": "Shubhendu",
    "role": "Engineer"
}


response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=body
)


result = response.json()
print(result)



post_id = 1
response_path_param = requests.get(
    f"https://jsonplaceholder.typicode.com/posts/{post_id}"
)

print(response_path_param.json())