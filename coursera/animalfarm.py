def d():
    animal="elephant"
    def e():
        nonlocal animal
        animal="Giraffe"
        print("Inside nested function: "+ animal)
    print("Before calling function: "+ animal)
    e()
    print("After nested function: "+ animal)
animal = "camel"
d()
print("Global Animal "+ animal)




import numpy as dn



import * from numpy



from numpy import *



from numpy import shape as s






