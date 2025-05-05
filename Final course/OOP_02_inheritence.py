#parent class
class Animal:
  def __init__(self, name):
    self.name = name
    print("Printing from parent class")
  def move(self):
    print("Moving")

#child class
class Dog(Animal):
  def __init__(self, name, breed, age):
#   def __init__(self,name):
    # Initialize attributes of the superclass
    super().__init__(name)
    # Additional attributes specific to Dog
    self.breed = breed
    self.age = age
    # self.name=name
    print("Printing from child class")

  def bark(self):
    print("Woof!")


my_dog = Dog("Jax", "Bulldog", 5)
# my_dog = Dog("Jax")
#inherited attribute
print(my_dog.name)

#Additional attributes
print(my_dog.breed)
print(my_dog.age)