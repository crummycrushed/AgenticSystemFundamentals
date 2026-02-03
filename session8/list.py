score = [2, 4, 5, 9, 5]
#index   0  1  2  3  4

# index always starts with 0

# name of the list [index]
#print(score[1])


value2 = score[3]
#print(value2)



# Modifying Lists
# adding at the end 
# removing some value
# replcating some value

marks = [34, 45, 78, 45, 64]
#index = 0   1    2   3   4
# add a new subject marks at the end , 89
# marks = [34, 57, 78, 45, 64, 89]
# print(marks[5]) #out of index error --> program terminates 
marks.append(89)
#print(marks[5])


# remove 45
#print(marks[1])
# [34, 45, 78, 45, 64, 89]
marks.remove(45)

#print(marks[1])
#print(marks[2])


#update a value ?/
attendance = [12, 43, 1, 54, 67]
#update 1 with 34
print(attendance[2])
attendance[2] = 34
print(attendance[2])



# List slicing (sub list)
world = [3, 4, 5, 2, 1]
# world_list_1 = [3, 4, 5]
# world_list_2 = [5, 2, 1]
# world_list_3 = [3, 4]

#list slicing
world_list_1 = world[0:3] #give me a list starting with index 0, and ending before 3
print(world_list_1)

world_list_2 = world[2:]
print(world_list_2)

world_list_3 = world[:2]
print(world_list_3)




#insert using index
abc = [1, 2, 3]
#abc.insert(0, 10) #insert(index, value)
#print(abc[0])

print(abc[1])
abc.pop(1)
print(abc[1])




c = [3, 4, 5]
empty_list = []

for i in c:
    empty_list.append(i)

print(empty_list)




d = [3,4,5]
#d = [1, 3, 4, 6, 5]
d.insert(0, 1)
d.insert(3, 6)

