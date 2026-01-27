marks = 50
another_marks = 30


if another_marks >= 40:  #30 >= 40--> false
    print("Student has passed") #
else:
    print("Student has failed")



temperature = 30
if temperature > 25:  #30 > 25
    print("It is warm outside")
else:
    print("It is not warm outside")



age = 16

if age >= 18:  # 16 >= 18
    print("Adult")



score = 65
# score >=90 print A
# if score >=75 then print B
# if socre >= 60  print C
# else print D

if score >= 90: #score = 92 >= 90 : False
    print("Grade A")
elif score >=75:  # else if  76 >=75
    print("Grade B")
elif score >=60:
    print("Grade C")
else:
    print("Grade D")




amount = 1200
# amount > 1100, then apply a discount of 100 rs
# else don't apply discount 
# print final amount 


if amount > 1100:
    amount_to_be_paid = amount - 100
    print(amount_to_be_paid)
else:
    print(amount)
