#!/usr/bin/env python3
# example with class
import fire

class Example(object):
    def hello(self, name='world'):
        """Says hello to the speficied name"""
        return 'Hello {name}!'.format(name=name)

def main():
    fire.Fire(Example)

if __name__ == '__main__':
    main()