#opg 1
def number_voweles(tekst):
    tekst = tekst.lower()
    voweles = ['a','e','i','o','u','y','æ','ø','å'] #Kunne lagd for loop med listen, For i in vowles
    number_voweles = tekst.count('a')\
                     +tekst.count('e')\
                     +tekst.count('i')\
                     +tekst.count('o')\
                     +tekst.count('u')\
                     +tekst.count('y')\
                     +tekst.count('æ')\
                     +tekst.count('ø')\
                     +tekst.count('å')
    return number_voweles


tekst = '''Norsk er et nordisk språk som er et av flere offisielle språk i Norge'''
print(number_voweles(tekst))
#opg 2

positions = '''\
== Positions ==
manager: Kari
treasurer: Ole
IT manager: Liv
parking officer: Kari
event manager: Liv
garden consultant: Kari
fire officer: Kari
'''
def get_positions(navn):
    resultat = []
    for line in positions.split('\n'):
        pos_line = line.split(": ")
        if len(pos_line) == 2 and navn in pos_line:
            resultat.append(pos_line[0])
    return resultat


print(get_positions('Kari'))
k = ('mom' in 'kardemomme')
q = sorted(['A','C','b','D'])
print(q)


