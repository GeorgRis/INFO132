
#opg 1

import math

def pi(d):
    desimal = round(math.pi, d)
    return desimal

y = input("Antall desimaler: ")

if y == "":
    print(pi(2))
elif int(y) > len(str(math.pi))-1:
    print("math.pi har ikke fleredesimaler, MAX 15")
    print(pi(int(y)))
else:
    print(pi(int(y)))

#opg 2
def convert(g, t = 'c'):
    if t == 'f':
        k = (g - 32) * 5 / 9
    else:
        k = (g*9/5)+32
    return k
print(convert(34, ''))

#opg 3a
balance = 500
interest_rate = 0.01
lr = []
def deposit(innskudd):
    global balance
    global interest_rate

    balance = balance + innskudd
    return balance

def withdrawal(utakk):
    global balance
    global interest_rate
    if utakk > balance:
        return balance
    else:
        balance = balance - utakk
        return balance

def calculate_interest(interest = interest_rate):
    global balance
    interest = balance * interest
    return interest

def interest_settlement():
    global balance
    balance = calculate_interest() + balance
    return balance
#b og c
def choose():
    global balance
    global interest_rate

    def liste(v):
        global lr
        change = v
        lr.append(change)



    print("------------------------")
    print("1 - show balance")
    print("2 - deposit")
    print("3 - withdraw")
    print("4 - interest settlement")
    print("5 - last changes")
    print("------------------------")

    valg = int(input("Choose action: "))

    if valg == 1:
        print("Balance: ", balance)
    elif valg == 2:
        amount = int(input("Amount: "))
        print(deposit(amount))
        if balance >= 1000000:
            interest_rate = 0.02
            print("Your interest got higher!")
        liste(amount)
    elif valg == 3:
        withdraw = int(input("Amout:"))
        print(withdrawal(withdraw))
        if withdraw > balance:
            print("Too large withdrawal, balance is: ",balance)

        if balance <= 1000000:
            interest_rate = 0.01
            print("And you have ordinary interest rate")
        else: print("You have higher interest rate")
        liste(-withdraw)

    elif valg == 4:
        print(interest_settlement())
        liste(calculate_interest())
    elif valg == 5:
        for x in lr[-3:]:
            if x > 0:
                print("+", x)
            else: print(x)

i = 0
while i == 0:
    choose()


#opg 4
import random
def three_random():
    tall1 = random.randrange(1, 10)
    tall2 = random.randrange(1, 10)
    tall3 = random.randrange(1, 10)
    liste = [tall1, tall2, tall3]
    liste.sort()
    return  liste

    '''
    midt = ""
   lavest = min(liste)
    hoyest = max(liste)
    for x in liste:
        if x != hoyest and x != lavest:
            midt = x
        else: '''

print(three_random())

