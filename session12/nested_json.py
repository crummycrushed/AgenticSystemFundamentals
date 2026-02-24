import json

json_response = '''
{
   "user": {
    "id": 123,
    "profile": {
        "name": "Shubhendu",
        "roles": ["admin", "editor"]
    }
   }
}
'''


parsed_dict = json.loads(json_response)
print(type(parsed_dict))

#print(parsed_dict)


name = parsed_dict["user"]["profile"]["name"]
print(name)



roles = parsed_dict["user"]["profile"]["roles"]
print(type(roles))
for i in roles:
    print(i)


val = parsed_dict.get("user").get("profile").get("abc")
print(val)

#roles[0], roles[1]



user = parsed_dict["user"]
#print(user)

profile = user["profile"]
#print(profile)

name = profile["name"] # parsed_dict["user"]["profile"]["name"]
#print(name)