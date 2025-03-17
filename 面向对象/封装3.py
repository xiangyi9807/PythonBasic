#! /usr/bin/env python
# author: vin

class Rectangle:
    def __init__(self, width, height):
        self.hidden_width = width
        self.hidden_height = height

    def get_width(self):
        return self.hidden_width

    def get_height(self):
        return self.hidden_height

    def set_width(self, new_width):
        self.hidden_width = new_width

    def set_height(self, new_height):
        self.hidden_height = new_height

    def get_area(self):
        return self.hidden_height * self.hidden_width

r = Rectangle(5,2)
print(r.get_area())