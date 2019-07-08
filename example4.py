#!/usr/bin/env python3
# multiple commands / functions using a dict to map to names
import fire

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

if __name__ == '__main__':
    fire.Fire({
        'add': add,
        'multiply': multiply
    })