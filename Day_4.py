# Randomisation:
# import random
# random.randint(a,b)

# Ex:
#import random
#random_integer=random.randint(0,100)
#print(random_integer)
# Returns random numbers from 0 to 100.

#Head or tails
# import random
# rand_no=random.randint(0,1)
# if rand_no==0:
#     print("Its a heads")
# else:
#     print("Its a tails")

# Lists

# Ex:1
# import random
# friends=["Aaron","Aliya","Angela","Ana"]
# print(random.choice(friends))

# Ex:2
# import random
# a=random.randint(0,4)
# friends=["Aaron","Aliya","Angela","Ana"]
# print(friends[a])

#Rock,paper and scissors
import random
user_choice=input("What do you chose? Type 0 for rock, 1 for paper, 2 for scissors")
computer_choice=random.randint(0,2)
print(f"Computer chose {computer_choice}\n")
if user_choice=="0" and computer_choice==1:
    print("Paper wins")
elif user_choice=="0" and computer_choice==2:
    print("Rock wins")
elif user_choice=="1" and computer_choice==2:
    print("Scissor wins")
elif user_choice=="2" and computer_choice==0:
    print("Rock wins")
elif user_choice=="2" and computer_choice==1:
    print("Scissor wins")
elif user_choice=="1" and computer_choice==0:
    print("Paper wins")
elif user_choice==computer_choice:
    print("Its a draw")
else:
    print("Please enter a valid number")

