age = 17
has_address = True


# if age is greater than or equals 18 and it has address , print("Entry allowed"), else denied
#  age >= 18 and has_address == True


# 20 >= 18 : True and False => False
# 17 >= 18 False and True => False
if age >= 18 and has_address:  # age >= 18 , 20 >= 18  True and True => True 
    print( "Entry Allowed")
else:
    print("Entry Denied")




balance = 100
price = 300
is_user_account_exists = True

# balanec >= price  price > 0   is_user_account_exists == print order places
# else order can't be placed


if balance >= price and price > 0 and is_user_account_exists:
    print("Order Placed")
else:
    print("Order can't be placed")





##### OR Operator

login_google = False
login_email = True


if login_google or login_email: # False or True ==> true
    print("user logged in")
else:
    print("user not able to login")




is_owner = True
is_admin = False

if is_owner or is_admin:  # True or False ==> True
    print("Access granted")
else:
    print("Access denied")




## Not operator


is_blocked = False

# if user is not blocked, access granted 


if is_blocked == True:
    print("access granted")



if not is_blocked:
    print("access granted")



marks = 95 
# if marks  < 95, print ("Better luck next time ")

if marks < 95:
    print("better luck next time")



completed = False 
# if user has not completed , print retry

if not completed:
    print("retry")