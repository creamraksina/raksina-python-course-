#ไฟล์นี้พูดถึงคุณสมบัติ OOP
# Inheritance คือการสร้างคลาสใหม่ โดยเอาคลาสที่มีอยู่แล้วมาประยุกต์ใช้

# Parent class (Base class)   คลาสแม่ = เป็นฐานเอาไปต่อยอด

class Animal:
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
    def make_sound(self):
        print(f"{self.name} makes a sound")

# Child class (Derived class) คลาสลูก
class Dog(Animal): #ในวงเล็บ คือรับฐานมาจากแม่อันไหน ถ้าไม่มีในวงเล็บสามารถสันนิฐานได้ว่ามันเป็นตัวแม่
    def __init__(self, name, breed):
        super().__init__(name, "Canine")  # Call parent constructor
        self.breed = breed
    
    # Method overriding
    def make_sound(self):
        print(f"{self.name} barks: Woof!")
    
    # New method specific to Dog
    def fetch(self):
        print(f"{self.name} is fetching the ball")

class Cat(Animal):
    
    def __init__(self, name, color):
        super().__init__(name, "Feline")
        self.color = color
    
    def make_sound(self):
        print(f"{self.name} meows: Meow!")
    
    def climb_tree(self):
        print(f"{self.name} is climbing a tree")

# Usage การใช้งาน
dog = Dog("Max", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

dog.eat()        # Inherited method
dog.make_sound() # Overridden method
dog.fetch()      # Dog-specific method

cat.make_sound() # Overridden method
cat.climb_tree() # Cat-specific method