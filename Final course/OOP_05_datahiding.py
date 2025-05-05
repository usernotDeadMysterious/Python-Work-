
# Data hiding is a key idea in making code with objects (like in games or apps) safer and cleaner. It means keeping some parts of an object private so that only certain parts of your code can change them. This helps prevent mistakes and keeps your code easy to manage.

 

# In this lesson, you'll explore how data hiding contributes to encapsulation in OOP, enhancing the security and robustness of your code.



class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    self.odometer = odometer

  def describe_car(self):
    print(self.year, self.model)

  def read_odometer(self):
    print("Odometer:", self.odometer, "miles")

my_car = Car('Audi', 2020, 15000)

my_car.describe_car()
my_car.read_odometer()

#changing a value of the attribute
my_car.odometer = 20000

my_car.read_odometer()

# In programming, sometimes it's crucial to 'protect' certain class attributes and methods from being accessed outside the class. This is called data hiding and ensures the integrity and security of the data, preventing unintended or harmful modifications.


# The next level of data hiding involves making an attribute private. This is achieved by prefixing the attribute name with two underscores (e.g., __attribute). In this case, unlike protected attributes, this is not just a convention - it limits its access outside the class through name mangling, enhancing data protection and encapsulation. This method is used for sensitive or internal data, strongly discouraging external access.


class Car2:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'private'
    self.__odometer = odometer



# Accessing a private attribute with double underscores from outside the class causes an error, but it's accessible within class methods. This demonstrates encapsulation, protecting sensitive data from external access and ensuring it's only reachable via specific methods, aligning with object-oriented programming principles.

class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'private'
    self.__odometer = odometer  

  def describe_car(self):
    print(self.year, self.model)

  def read_odometer(self):
    print("Odometer:", self.__odometer, "miles")

my_car = Car('Audi', 2020, 15000)

#accesing using name mangling
print(my_car._Car__odometer)