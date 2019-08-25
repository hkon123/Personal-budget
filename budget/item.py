import numpy as np



class Item(object):
    num_items = 0
    total_value = 0

    def __init__(self, name, price, priority):
        self.name = name
        self.price = price
        self.priority = priority
        self.update_class()

    def update_class(self):
        Item.num_items +=1
        Item.total_value +=self.price
