# histogram  a word that has no repeating alphabets
# find input word is histogram or not

inp = input ()
counter =0
for y in inp:
  counter+= 1
flag = 0
def disp():
 print("true")  
string = ''

alphabet = 'abcdefghijklmnopqrstuvwxyz'
c = 0
for i in alphabet : 
  for j in inp:
   if j == i:
     c+=1
     if j in string:
       flag = 1
       
     else:
      string += j
      flag =0
     
print(string)
print(c)

if flag == 1:
   disp()
else :
  print("false")

