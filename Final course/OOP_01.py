class Car:
  # Initialize attributes
  def __init__(self, brand, color):
    # Assign values to attributes
    self.brand = brand
    self.color = color
  def honk(self):
    print("Beep beep!")
# Create an object of the Car class
my_car = Car('Audi', 'yellow')

print(my_car.brand)
print(my_car.color)

my_car.honk()

#function
def greet():
  print("Welcome!")

#list
prices = [55, 68, 77, 36]

#data types
x = 5
city = "London"
is_open = True


print(type(greet))
print(type(prices))
print(type(x))
print(type(city))
print(type(is_open))