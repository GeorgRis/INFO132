#opg 1
#for loop
def fact(n):
    f=1
    for x in range(1,n+1):
        f = f*x
    return

#while loop er akkurat samme nesten, tar ganger tall
def fact(n):
    f = 1
    while n >= 1:
        f = f*n
        n -= 1
    return f

#opg 2
class Monarch:
    def __init__(self, land, navn, aar):
        self.land = land
        self.navn = navn
        self.aar = aar

    def acceded(self):
        print("King", self.navn, "of", self.land, "acced to the throne in", self.aar)

haakon = Monarch('Norge','Haakon VI', '1905')
olav = Monarch('Norge', 'Olav V', '1957')
harald = Monarch('Norge', 'Harald VI', '1991')
royal_line = [haakon, olav, harald]


"""for x in range(len(royal_line)):
    royal_line[x].acceded()
    """ 
for x in royal_line:
    x.acceded()





