import math


class Expression():
    def eval(self):
        pass
    # collect all the numbers into a set

    def collect_numbers(self):
        v = set()
        lr = [self.operand2,self.operand1]
        for i in lr:
            v = v.union(i.collect_numbers())
        return v
        # TODO: implement this method in proper sub classes


class Constant(Expression):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

    def __str__(self):
        return str(self.value)

    def collect_numbers(self):
        # singleton set
        return {self.value}


class BinaryExpression(Expression):
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2


class PlusExpression(BinaryExpression):
    def __init__(self, operand1, operand2):
        super().__init__(operand1, operand2)

    def eval(self):
        return self.operand1.eval() + self.operand2.eval()

    def __str__(self):
        return f"({self.operand1}) + ({self.operand2})"


class MinusExpression(BinaryExpression):
    def __init__(self, operand1, operand2):
        super().__init__(operand1, operand2)

    def eval(self):
        return self.operand1.eval() - self.operand2.eval()

    def collect_numbers(self):
        return {self.operand1.eval(), self.operand2.eval()}

    def __str__(self):
        return f"({self.operand1}) - ({self.operand2})"


class MultiplyExpression(BinaryExpression):
    def __init__(self, operand1, operand2):
        super().__init__(operand1, operand2)

    def eval(self):
        return self.operand1.eval() * self.operand2.eval()

    def __str__(self):
        return f"({self.operand1}) * ({self.operand2})"

    def collect_numbers(self):
        return Expression.collect_numbers(self)


class DivideExpression(BinaryExpression):
    def __init__(self, operand1, operand2):
        super().__init__(operand1, operand2)

    def eval(self):
        return self.operand1.eval() / self.operand2.eval()

    def __str__(self):
        return f"({self.operand1}) / ({self.operand2})"

    def collect_numbers(self):
        return Expression.collect_numbers(self)


class NaryExpression(Expression):
    # operands is a list of expressions
    def __init__(self, *operands):
        self.operands = operands

    def collect_numbers(self):
        s = set()
        o = self.operands
        for j in o:
            for i in j:
                s = s.union(i.collect_numbers())
        return s
    # TODO: insert your code here


class MaxExpression(NaryExpression):
    def __init__(self, *operands):
        super().__init__(operands)

    def eval(self):
        lr = []
        for j in self.operands:
            for i in j:
                lr.append(i.eval())
        return max(lr)

    def __str__(self):
        lr = []
        for i in self.operands:
            for j in i:
                j = str(j)
                lr.append(j)
        lr = tuple(lr)
        return f"Max: ({lr})"

    def collect_numbers(self):
        return NaryExpression.collect_numbers(self)

    # TODO: insert your code here


class MinExpression(NaryExpression):
    def __init__(self, *operands):
        super().__init__(operands)

    def eval(self):
        lr = []
        for j in self.operands:
            for i in j:
                lr.append(i.eval())
        return min(lr)

    def __str__(self):
        lr = []
        for i in self.operands:
            for j in i:
                j = str(j)
                lr.append(j)
        lr = tuple(lr)
        return f"Min: ({lr})"

    def collect_numbers(self):
        return NaryExpression.collect_numbers(self)
    # TODO: insert your code here


if __name__ == '__main__':
    One = Constant(1)
    Two = Constant(2)
    Three = Constant(3)
    OneThousand = Constant(1000)
    Pi = Constant(round(math.pi, 2))

    expr1 = MultiplyExpression(MultiplyExpression(Three, Three), Pi)  # 3 * 3 * pi
    expr2 = DivideExpression(OneThousand, Three)  # 1000 * 3
    expr3 = MinusExpression(OneThousand, Two)  # 1000 - 2
    expr_min = MinExpression(expr1, expr2, expr3)
    expr_max = MaxExpression(expr1, expr2, expr3)

    for expr in [expr1, expr2, expr3, expr_min, expr_max]:
        print(f"{expr} = {expr.eval()}, with numbers {expr.collect_numbers()}")
        print()
