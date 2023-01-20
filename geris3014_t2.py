#Task 1

#import from library
import math
import random

#Variables
r = float(input("Radius: "))
a = "{:.3f}".format(math.pi*r**2)

print("The ara of a circle with radius ",r, " is ", a )
#space between program
print("\n")

#Task 2
melding = str(input("Please enter a sentence: "))
#Count spaces
mellomrom = melding.count(" ")
print(len(melding)-mellomrom)
guess = input("Guess the number of letters in the sentence: ")
#Length sentence-spaces
if float(guess) == len(melding)-mellomrom:
    print("That's True!" )
else:
    print("That's false!")

print("\n")

#task 3
nummer = str(input("Please input a number:"))
#random number generate from 0-50
tilfeldig = str(random.randrange(0,10))
sammen = nummer+tilfeldig
print(sammen,"/", nummer,"=", int(sammen)/int(nummer))












