#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    negative = "%d is negative" %(number)
    print(negative)
elif number == 0:
    zero  = '%d is zero' %(number)
elif number > 0:
    positive = "%d is positive" %(number)
    print(positive)
