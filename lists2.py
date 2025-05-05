vehicles = [1,2]
colors= [3,4]
for vehicle in vehicles:
  for color in colors:
    print(vehicle, color)

products = ['ball', 'gloves']
colors = ['red', 'blue']
for i in products :
  for j in colors:
    print(j, i)


grades = [70,60,50,34,5,67,6,7,655,66,90]
for grade in grades:
  if grade <= 50:
    continue
  print(grade)

word = 'vehicle'
print(word.find())