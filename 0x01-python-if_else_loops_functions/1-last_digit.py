#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d} is ".format(number), end="")
if number < 0:
    num = ((-number) % 10) * -1
else:
    num = number % 10
if num > 5:
    print("{:d} and is greater than 5".format(num))
elif num == 0:
    print("{:d} and is 0".format(num))
else:
    print("{:d} and is less than 6 and not 0".format(num))
