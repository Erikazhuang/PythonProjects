class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []  #import create list for each dog, not a shared list across dogs

    def addTrick(self, trick):
        self.tricks.append(trick)

    
    