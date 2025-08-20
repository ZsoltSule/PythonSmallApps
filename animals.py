class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    
    def speak(self):
        print("I dont know what to say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
    def speak(self):
        print("Meow")
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):    
    def speak(self):
        print("Woof")

class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.speak()
c = Cat("Norton", 4, "Black")
c.show()
c.speak()
d = Dog("Goofy", 6)
d.show()
d.speak()
f = Pet("Bubles", 2)
f.speak()