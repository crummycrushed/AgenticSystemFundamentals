# A function is a code that runs only when u call it 

# Ex: 1
def greet(): #def <function_name>():
    print("hello")


greet()



def say_hi():
    print("hi")





# parameters and arguments

# parameter is like an empty box
# argumenr --> value inside the box
def greetings(name): #name=shubhendu. --> name is parameter
    print("Hello", name) # hello shubhendu



greetings("Shubhendu") # shubhendu --> arguments
greetings("Rahul")
greetings("Ali")


# name = Shubhendu
# name = Rahul



# Multiple parameter 

# calculate a price of a product whose unit price is 300rs, and quantityu is 3

# functions can accept multiple inputs

def calculate_total(unit_price, quantity): #unit_price=300, quantity=3
    total = unit_price * quantity # total = 300 * 3
    print(total) # total = 900

calculate_total(300, 3)