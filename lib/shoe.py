#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        if isinstance(size, int):
            self.size = size
        else:
            print("size must be an integer")

    @property
    def condition(self):
        return self.condition
    
    @condition.setter
    def condition(self, new_condition):
        self.condition = new_condition

    def cobble(self):
        self.condition = 'New'
        return "Your shoe is as good as new!\n"