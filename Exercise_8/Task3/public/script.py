#!/usr/bin/env python3

class Fridge:
    
    def __init__(self):
        self.__items = []
        self.__product_index = -1 # Variable used for iterator

    def store(self, product):
        self.__items.append(product)
        self.__items.sort()

    def __iter__(self):
        return self

    def __next__(self):
        self.__product_index += 1
        try: 
            return self.__items[self.__product_index]
        except: 
            raise StopIteration

    def __len__(self):
        return len(self.__items)

    def take(self, product):
        try: 
            self.__items.remove(product)
            return product
        except: 
            raise Warning("Error 404: Item not found.")

    def find(self, name):
        for item in self.__items: 
            if item[1] == name: 
                return item
        return None

    def take_before(self, date):
        out = []
        # I cannot delete items from the list, while looping through it. That's why I need two loops.
        for product in self.__items:
            if product[0] < date: 
                out.append(product)
        for expired_item in out: 
            self.__items.remove(expired_item)
        return out