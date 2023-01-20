#array
navn = ["Georg", "Mykjåland", "Risøy"]

print(navn[0])
print(navn[1])
print(navn[2])

#while loop
i = 0
while i < len(navn):
    print(navn[i])
    i += 1
else:
    #task 2
    print("Task 2a and b")
    #Values from example and Valuta signs
    euro = ("\N{euro sign}")
    dol = ("\N{dollar sign}")

    #int(input)=Input with number
    penger = float(input('Hvor mye vil du konvertere I antall euro eller dollar'))

    #Converting Number
    NokToEuro = 0.101
    NokToDol = 0.102
    #"{:.2f}".format = 2 desimalpoint
    print("{:.2f}".format(penger * NokToEuro), euro," er", penger,"kr i euro to NOK")
    print("{:.2f}".format(penger * NokToDol), dol," er", penger, "kr i dollar to NOK")







