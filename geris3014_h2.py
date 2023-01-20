#opg 1
class SquareMatrix:
    def __init__(self, order):
        self.order = order
        self.rows = [
            [0 for j in range(order)]
            for i in range(order)
        ]

    def __str__(self):
        return ("\n".join(
            [
                " ".join([str(stri) for stri in row])
                for row in self.rows
            ]
        ))

    def set_value(self, i, j, value):
        row = self.rows
        row[i].insert(j,value)
        del row[i][3]

    def get_value(self, i, j):
        return self.rows[i][j]

    def max(self):
        lrmax = []
        for row in self.rows:
            lrmax.append(max(row))
        return max(lrmax)

    def min(self):
        lrmin = []
        for row in self.rows:
            lrmin.append(min(row))
        return min(lrmin)

    def trace(self):
        sumed = 0
        for x in range(self.order):
            sumed += self.rows[x][x]
        return sumed

    def summary(self):
        return f'order: {self.order}, max: {self.max()}, min: {self.min()}, trace: {self.trace()}'

    def save(self, filename):
        text_file = open(filename, 'w')
        text_file.write(SquareMatrix.__str__(self))
        text_file.close()

    @classmethod
    def parse(cls, text):
        lr_parse = []
        for rows in text.split('\n'):
            values = rows.split(" ")
            lr_parse.append(values)
        cls.rows = lr_parse

        order = len(lr_parse)
        i = 0
        m = SquareMatrix(int(order))
        while i <= order-1:
            for j in range(order):
                value = cls.get_value(cls,i,j)
                m.set_value(i,j,int(value))
            i += 1

        return m

    @classmethod
    def load(cls, filename):
        m3 = open(filename,'r')
        m3_text = m3.read()
        m3 = SquareMatrix.parse(m3_text)
        return m3



m1 = SquareMatrix(3)
m1.set_value(0, 0, 1)
m1.set_value(1, 1, 1)
m1.set_value(2, 2, 1)
print("--m1--")
print(m1)
print(m1.summary())

m2_text = """\
1 2 3
4 5 6
7 8 9"""
print("--m2--")
m2 = SquareMatrix.parse(m2_text)
print(m2)
print(m2.summary())

m2.save("m3.txt")

print("--m3--")
m3 = SquareMatrix.load("m3.txt")
print(m3)
print(m3.summary())


