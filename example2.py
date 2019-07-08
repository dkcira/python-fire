#!/usr/bin/env python3
# example with function
import fire

def hello(name):
    return 'Hello {name}!'.format(name=name)

if __name__ == '__main__':
    fire.Fire(hello)