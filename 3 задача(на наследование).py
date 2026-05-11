class Animal:
    def make_sound(self):
        return "Some animal sound"
    def move(self):
        return "moves"
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"
    def move(self):
        return "runs"
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    def move(self):
        return "walks silently"
class Cow(Animal):
    def make_sound(self):
        return "Moo!"
    def move(self):
        return "walks slowly"
print(Dog().make_sound())  # "Woof! Woof!"
print(Dog().move())  # "runs"
print(Cat().make_sound())  # "Meow!"
print(Cat().move())  # "walks silently"
print(Cow().make_sound())  # "Moo!"
print(Cow().move())  # "walks slowly"
print(Animal().make_sound())  # "Some animal sound"
print(Animal().move())  # "moves"
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.make_sound()}, {animal.move()}")