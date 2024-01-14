from random import choice
from vars import *


class Pixel:
    def __init__(self, display, pos, color):
        self.pos = pos
        self.color = color
        self.display = display

    def update(self):
        pass

    def draw(self):
        self.display.set_at(self.pos, self.color)


class Block(Pixel):
    def __init__(self, display, pos, color):
        super().__init__(display, pos, color)
        self.typ = "block"


class Liquid(Pixel):
    def __init__(self, display, pos, color):
        super().__init__(display, pos, color)
        self.typ = "liquid"

    def update(self):
        pass


class Sand(Pixel):
    def __init__(self, display, pos, color):
        super().__init__(display, pos, color)
        self.typ = "sand"

    def update(self):
        pass


class Pixels:
    def __init__(self, display, delay=0):
        self.display = display
        self.pixels = {}
        self.delay = delay
        self.counter = 0

    def update(self):
        self.counter += 1
        if self.counter < self.delay:
            return None
        else:
            self.counter = 0

        for key in list(self.pixels.keys()):
            pixel = self.pixels[key]

            if pixel.typ == "sand":
                x, y = pixel.pos
                if (x, y + 1) not in self.pixels:
                    pixel.pos = (x, y + 1)
                    self.pixels[(x, y + 1)] = self.pixels.pop((x, y))
                    continue
                left = (x - 1, y + 1) not in self.pixels
                right = (x + 1, y + 1) not in self.pixels
                direction = 0
                if left and right:
                    direction = choice([-1, 1])
                elif left:
                    direction = -1
                elif right:
                    direction = 1

                if direction and (x + direction, y + 1) not in self.pixels:
                    pixel.pos = (x + direction, y)
                    self.pixels[(x + direction, y)] = self.pixels.pop((x, y))

    def draw(self):
        for pixel in self.pixels.values():
            pixel.draw()

    def add(self, pos, typ):
        if typ == "block":
            self.pixels[pos] = Block(self.display, pos, GREY)
        elif typ == "sand":
            self.pixels[pos] = Sand(self.display, pos, YELLOW)
        elif typ == "liquid":
            self.pixels[pos] = Liquid(self.display, pos, BLUE)



