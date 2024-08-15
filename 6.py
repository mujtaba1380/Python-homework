class Animal:
    def speak(self):
        print("this is the animal sound.")
class Dog(Animal):
    def speak(self):
        print("the dog speak is bark")
class Cat(Animal):
    def speak(self):
        print("the cat speak is meow")
dog = Dog()
cat = Cat()
dog.speak()
cat.speak()