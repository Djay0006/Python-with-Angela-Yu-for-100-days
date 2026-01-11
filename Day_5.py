# loops

# For loop

# maximum in the list:
# Student_scores=[150,142,185,120,171,184,149,24,59,68,199,78,65,89,86]
# maxi=0
# for score in Student_scores:
#     if score>maxi:
#         maxi=score
# print(maxi)

# Carl guess challenge:
# sum_of_no=0
# for number in range(1,101):
#     sum_of_no+=number
# print(sum_of_no)

# maxi=0
# for number in range(1,101):
#     if maxi<number:
#         maxi=number
# print(maxi)

#FizzBuzz

# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number%3==0:
#         print("Fizz")
#     elif number%5==0:
#         print("Buzz")
#     else:
#         print(number)

#Password generator
print("Welcome to password generator")
import random
a=0
b=0
no_letters=int(input("How many letters would you like in your passowrd?\n"))
if no_letters%2!=0:
    a=int(no_letters/2)
    b=int((no_letters/2)+1)
else:
    no_letters==no_letters
no_symbols=int(input("How many symbols would you like?\n"))
no_numbers=int(input("How many numbers would you like?\n"))
symbol_list=["!","@","#","$","%","^","&","*","(",")","+"]
password=[]
for i in range(0,no_numbers):
    random_no =random.randint(0,9)
    password.append(str(random_no))
for i in range(0,a):
    random_no=random.randint(65,90)
    password.append(chr(random_no))
for i in range(0,b):
    random_no = random.randint(97, 122)
    password.append(chr(random_no))
for i in range(0,no_symbols):
    a = random.randint(0, 10)
    password.append(str(symbol_list[a]))
random.shuffle(password)
password_new=""
for char in password:
    password_new+=char
print(f"Your password is {password_new}")



