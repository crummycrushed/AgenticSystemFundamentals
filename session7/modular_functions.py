# Get user name from terminal and print it by converting into upper case ?
# str.upper() str=name , NAME


# get_name
# make_upper


def get_name(): #1st this is called
    name = input("Enter name: ")
    return name #shubhendu

def make_upper(name): #name = shubhendu
    #upper_Case = name.upper()
    #return upper_Case
    return name.upper() #SHUBHENDU


name = get_name() #first function #name = shubhendu
result = make_upper(name) #make_upper("shubhendu") #result = "SHUBHENDU"
print(result) #SHUBHENDU