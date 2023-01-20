#opg 1
def verdi_1(x, y):
    tfx = x!=7
    tfy = y <= 50
    T_or_F = tfx and tfy
    return  T_or_F


x = 9
y = 66
print(verdi_1(x,y)) #Print false siden tfy er false

def verdi_2(x, y):
    tf_0 = x > 7 or 50<y
    tf_1 = x >y or y < 100
    t_or_f = tf_0 and tf_1
    return t_or_f


print(verdi_2(x, y)) #Printer true

#opg 2
def tulleby(a,lived):
    if a >= 25:
        if lived >= 9:
            return ("You can become mayor")
        else:
            return ("Try agian in " + str(9-lived) + " years")
    else:
        return ("Try agian in " + str(25-a) + " years")


a = int(input("Please state your age: "))
lived = int(input("How long have you lived in tulleby: "))
print(tulleby(a, lived))

#opg 3
x = int(input('Number: '))
if x > 5 and x < 10:
        print('6, 7, 8 or 9')
else:
    print('between 5 and 10')

#opg 4
def multi():
    print("   |    1   2   3   4   5   6   7   8   9 ") #fant ikke måte å få det på med "for"
    print("---+--------------------------------------") # og ble et fint mellomrom mellom de da
    for i in range(1,10):
        print()
        print(i, " |", end ="\t")
        for j in range(1,10):
            print(i*j, end ="\t")

multi()



