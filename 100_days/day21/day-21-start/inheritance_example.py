class Animal:
    def __init__(self):
        self.eyes = 2
    def breath(self):
        print('inhale')

class Fish(Animal):
    def __init__(self):
        super().__init__() # allows anything created from fish class to inherit animal methods and props

    def swim(self):
        print('moving')

    def breath(self):
        super().breath()
        print('doing underwater') # fish own unique behavior for breath method in addition to animal breathe