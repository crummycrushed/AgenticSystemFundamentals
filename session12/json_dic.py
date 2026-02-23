import json


data =  {
    "name": "Shubhendu",
    "age": 30
}

json_string  = json.dumps(data)


## To write json into a file, config.json

with open("config.json", "w") as f:
    json.dump(data, f)



# dumps vs dump
# writes jsons directly to a file
# dumps : Return json as string