# name, age, phone


user = {
   
    "name": "Alice",
     #key.    #value
    "age": 30,
    "phone": 1234354,
    "is_valid_user": False
}


print(user["name"])
print(user["age"])


#add a new key ?
user["email"] = "a@gmail.com"
print(user["email"])

user["phone"] = 234345643
print(user["phone"])


#print(user)

    #var  #var
for key, value in user.items():
    if key == "is_valid_user" and value == False:
        print("user is not authenticated")    
    print(key, value) #key, value




user2 =  {
    "name": "Avishkar",
    "age": 21,
    "phone": 92324123
}


#key must be unique


row1 = {
   "col1" : "valu1",
   "col2": "value2",
   "col3": "value3"
}