import os
import base64

class Index:
    def __init__(self, name):
        self.name = name
        self.table = {}

    def add(self, key, value: Pointer):
        self.table[key] = value

    def retrieve(self, key):
        return self.table[key]

class Pointer:
    # i don't know the initial values which it should have
    def __init__(self):
        pass

    # it should save a pointer to the data file
    def point(self):
        pass

    # it should remove the pointer to the already added data file
    def pop(self):
        pass

    # it should retrieve a specific value from the data file
    def retrieve(self, id):
        pass

