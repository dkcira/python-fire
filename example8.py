#!/usr/bin/env python3
# function chaining with a class whose methods return self
import fire

class BinaryCanvas(object):
    """A canvas with which to make binary art, one bit at a time."""

    def __init__(self, size=10):
        self.pixels = [['O'] * size for _ in range(size)]
        self._size = size
        self._row = 0 # the row of the cursor
        self._col = 0 # the column of the cursor
        print(f'size = {self._size}')

    def __str__(self):
        return '\n'.join(' '.join(str(pixel) for pixel in row) for row in self.pixels)

    def show(self):
        print(self)
        return self

    def move(self, row, col):
        self._row = row % self._size
        self._col = col % self._size
        return self

    def on(self):
        return self.set('X')

    def off(self):
        return self.set('O')

    def set(self, value):
        self.pixels[self._row][self._col] = value
        return self

if __name__ == '__main__':
    fire.Fire(BinaryCanvas)