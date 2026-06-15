class Animal:
    def __init__(self):
        print('Animal: __init__ called ...')

class Bat(Animal):
    def __init__(self):
        super().__init__()
        print('Bat: __init__ called ...')

class Cat(Animal):
    def __init__(self):
        super().__init__()
        print('Cat: __init__ called ...')

class Dog(Bat, Cat):
    def __init__(self):
        super().__init__()
        print('Dog: __init__ called ...')

if __name__ == '__main__':
    my_dog = Dog()

    print(Dog.mro())