class Animal:
    def speak(self):
        print("Animal sound")
class Dog(Animal):
    def speak(self):
        print("Bark")
dog = Animal()
dog.speak()
