# basic math in python
# operators in python

a = 11
b = 3


sum = a + b  #addition
print(sum)


sub = b - a #subtraction
print(sub)

mul = a * b #multiplication
print(mul)


div = a / b #division
print(div)



# floor --> nearest lowest integer corresponding to float value
# 3.333333 --> 3
# ceil --> nearest greated interger correspond to float value
# 3.33333 -> 4


nearest_int_div = a // b 
print(nearest_int_div)

# 11 / 3 
# quotient = 3
# remainder = 2


remainder = a % b  #remainder
print(remainder)



c = 2
d = 3
# 2 to the power 3
exponent = c ** d
print(exponent)



price = 50
quantity = 4
total = price * quantity
print(total)





total_marks = 450
subjects = 5
average = total_marks / subjects
print(average)


## order of executions 

# 1, parenthesis 
# 2. Exponents
# 3. Multiplication / Divistion
# 4 Addition / subtraction 



result = (2 + 3) * 4 + 6 / 2

#  5 * 4 + 6 / 2
# 20  + 3.0
# 20.0 + 3.0
# 23.0
print(result)

