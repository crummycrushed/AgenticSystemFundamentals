
#variable = open -- connection --> file, read mode
from venv import logger


file = open("/Users/priyanshu/Documents/AgenticSystemFundamentals/session9/hello.txt", "r")
#print(file.read()) #read 
file.close()


# read everything , we basically use file.read()


#file = open("/Users/priyanshu/Documents/AgenticSystemFundamentals/session9/hello.txt", "r")
#print(file.read()) #read 
# index our error 
# error happens  ???

#file.close() # before closing the files



# with statement 

# file = open()
with open("/Users/priyanshu/Documents/AgenticSystemFundamentals/session9/hello.txt", "r") as i:
    content = i.read()
    #print(content)



#python gurantees: file close, even if crash happens, even if exception occues


# read line by line
with open("/Users/priyanshu/Documents/AgenticSystemFundamentals/session9/hello.txt", "r") as file:
    for line in file:
        content = line
        if content == "Shubhendu":
            print("inside shubhendu loop")
            continue
        print(content)


## readlines() --> readlines stores all lines into a list

with open("/Users/priyanshu/Documents/AgenticSystemFundamentals/session9/hello.txt", "r") as file:
    lines = file.readlines()
    for i in lines:
        print(i.strip())

    
