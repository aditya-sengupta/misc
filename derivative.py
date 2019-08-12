import numpy as np

class Function:

    def __init__(self, fn, rep, type='b', fn1=None, fn2=None):
        self.fn = fn
        self.rep = rep
        self.type = type
        self.fn1 = fn1
        self.fn2 = fn2

    def __repr__(self):
        return self.rep

    def eval(self, x):
        return self.fn(x)

    @staticmethod
    def const(c):
        return Function(lambda x: c, str(c))

    #x, ln, sin, cos primitive
    x = Function(lambda x: x, 'x')
    log = Function(lambda x: np.log(x), 'log', 'm')
    sine = Function(lambda x: np.sin(x), 'sin', 'm')
    cosine = Function(lambda x: np.cos(x), 'cos', 'm')

    @staticmethod
    def sum(fn1, fn2):
        if fn1.rep == '0':
            return fn2
        elif fn2.rep == '0':
            return fn1
        return Function(lambda x: fn1.eval(x) + fn2.eval(x), fn1.rep + " + " + fn2.rep, 's', fn1, fn2)

    @staticmethod
    def exp(fn1, fn2): # get a^x by const^x, or get x^n by x^const
        if fn1.rep == '1':
            return fn1
        elif fn1.rep == '0':
            if fn2.rep == '0':
                return Function.const(1)
            else:
                return Function.const(0)
        else:
            return Function(lambda x: fn1.eval(x) ** fn2.eval(x), fn1.rep + " ** " + fn2.rep, 'e', fn1, fn2)

    @staticmethod
    def __add__(fn1, fn2):
        return sum(fn1, fn2)

    @staticmethod
    def __pow__(fn1, fn2):
        return exp(fn1, fn2)

    @staticmethod
    def prod(fn1, fn2):
        if fn1.rep == '1':
            return fn2
        elif fn2.rep == '1':
            return fn1
        elif fn1.rep == '0':
            return fn1
        elif fn2.rep == '0':
            return fn2
        return Function(lambda x: fn1.eval(x) * fn2.eval(x), "(" + fn1.rep + ") * (" + fn2.rep + ")", 'p', fn1, fn2)

    @staticmethod
    def compose(fn1, fn2):
        if fn1.type == 'b':
            if fn1.rep == 'x':
                return fn2
            else:
                return fn1
        return Function(lambda x: fn1.eval(fn2.eval(x)), "(" + fn1.rep + ")(" + fn2.rep + ")", 'c', fn1, fn2)

    def derivative(self):
        if self.type == 'b':  # basic/primitive: x or constant
            if self.rep == 'x':
                return Function.const(1)
            else: # it's a constant
                return Function.const(0)
        elif self.type = 'm': # math
            if self.rep == 'log':
                return Function.exp(x, Function.const(-1))
            elif self.rep == 'sin':
                return cosine
            elif self.rep == 'cos':
                return Function.prod(Function.const(-1), sine)
        elif self.type == 's': # sum
            return Function.sum(self.fn1.derivative(), self.fn2.derivative())
        elif self.type == 'p': # product
            return Function.sum(Function.prod(self.fn1.derivative(), self.fn2), Function.prod(self.fn1, self.fn2.derivative()))
        elif self.type == 'c': # composition
            return Function.prod(Function.compose(self.fn1.derivative(), self.fn2), self.fn2.derivative())
        elif self.type == 'e': #exponentiation
            exponent = Function.prod(self.fn2, Function.compose(log, self.fn1)))
            return Function.prod(self, exponent.derivative())
