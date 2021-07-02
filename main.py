#Guessing Number difficulty easy
import math
import random

print(" WELCOME TO GUESSING Game")
Name = input(" ENTER YOUR GAME \n")
print("  Welcome : " + Name)

lowerbound = int(input("Enter The Lower limit\n"))
upperbound = int(input("Enter The Upper limit \n"))

X = random.randint(lowerbound,upperbound)

print("\n\t You got ",round(math.log(upperbound - lowerbound + 1,2)),"Chances to the number ")

count = 0

while count<math.log(upperbound - lowerbound+1,2):
    Number_guessed = int(input("Enter The Number"))
    count+=1
    if X == Number_guessed :
        print("CONGRATULATION , YOU WON THE GAME")
        break
    elif X > Number_guessed:
        print("The Number You Guessed is small")

    elif X < Number_guessed:
        print("The Number You Guessed is big ")







