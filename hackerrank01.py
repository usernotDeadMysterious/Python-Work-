# #!/bin/python3

# # import math
# # import os
# # import random
# # import re
# # import sys



# #
# # Complete the 'fizzBuzz' function below.
# #
# # The function accepts INTEGER n as parameter.
# # n = int(input())

# def fizzBuzz(n):
#     # Write your code here
#     # self.n = n
#     for i in range(1, n + 1):
#         if i % 3 ==0 and i % 5 ==0:
#             print("FizzBuzz")
#         elif i % 3==0:
#             print("Fizz")
#         elif i % 5 ==0:
#             print("Buzz")
#         else:
#             print(i)
        
#     # if __name__ == '__main__':
    
#     n = int(input().strip())

#     fizzBuzz(n)




def fizzBuzz(n):
    # Loop through numbers from 1 to n
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:  # Divisible by both 3 and 5
            print("FizzBuzz")
        elif i % 3 == 0:  # Divisible by 3
            print("Fizz")
        elif i % 5 == 0:  # Divisible by 5
            print("Buzz")
        else:
            print(i)

# Input from user
n = int(input("Enter a number: ").strip())
fizzBuzz(n)
