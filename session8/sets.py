tags = {"ai", "python", "data", "data"}

print(tags)

#add :
tags.add("shubhendu")
tags.remove("ai")
for i in tags:
    print(i)

a = {1, 2, 3}
b = {3, 4 , 5}

# {1, 2, 3, 4, 5}

c = a | b
print(c)


# common element between a & b
d = a & b
print(d)


# diff betwwen a and b 
e = b - a
print(e)
