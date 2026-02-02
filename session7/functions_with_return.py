def add(a, b): # a = 2, b = 3
    sum = a + b # sum = 5
    return sum #return 5. # dead end 
    print(sum)

def subtract(a, b): # a = 5, b =1
    diff = a - b #5 - 1 = 4
    print(diff) #4


output = add(2, 3) #sum = 5
# print(output)
subtract( output, 1) # subtract(5, 1)




# functions can return early to stop executions
def check_access(is_verified):  #is_verified = False
    if not is_verified: # not False  if true:
        return "Access Denied" # return access deined
    else:
        print("Nice")
        print("hello")
        print("bye")
        return "Access granted"
    

access = check_access(False) #access = "Accccess denied"
print(access)




# Python allows returning multiple values 
def greetings(name):
    greeting_sentence = "hello " + name
    return name, greeting_sentence


name, sentenece = greetings("Shubhendu")
print(name)
print(sentenece)





# 0 + 1 + 2 + 3
def sum_and_average(range_value): #range_value = 4
    sum = 0                                             #i
    for i in range(range_value): #for i in [0, 1, 2, 3]
        sum = sum + i # sum = 6

    average = sum / range_value

    return sum, average

    # return hra, base_salary, ctc
  
#h=hrs, base=base_salary, ctc=crc
#h, base, ctc = calculate_salary("shubhendu")
s, avg = sum_and_average(4)
print(s)
print(avg)







def show_salary(username):
    ctc = 120000
    base = 70000
    hra = 30000
    pf = 20000

    return ctc, base, hra, pf




ctc, base, hra, pf = show_salary("shubhendu")
print("CTC:", ctc)
print("Base:", base)
print("HRA:", hra)
print("PF:", pf)