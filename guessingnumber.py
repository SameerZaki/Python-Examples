def guess_game():

import random

rand_num = random.randint(1,10)
count = 0
my_num = 0

while my_num != rand_num and my_num != "exit":

my_num = input("I am thinking of a number between 1 & 9. Or 'exit' ")
if my_num.lower() == "exit":
break

my_num = int(my_num)

if my_num < 1 or my_num > 9:
print ("That is not a valid option, try again.")
continue

elif my_num > rand_num:
count += 1
print ("My number is lower...")
continue

elif my_num < rand_num:
count += 1
print ("My number is bigger...")
continue

elif my_num == rand_num:
count += 1
print (f"{my_num} Correct! You guessed right in {count} guesses")

#Author : Sameer Diwan