#!/usr/bin/env python3
# using an object of a class
import fire

class Calculator(object):

    def add(self, x, y):
        return x + y
    
    def multiply(self, x, y):
        return x * y



if __name__ == '__main__':
    calculator = Calculator()
    fire.Fire(calculator)