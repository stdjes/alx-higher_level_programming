#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Deal with negative number (because of negative modulo error issues)
if (number < 0): 
    last_digit = (-1 * number) % 10 #convert negative number to positive, then find modulo
    last_digit *= -1 #convert back to negative remainder

else:
    last_digit = number % 10 #for positive numbers

if (last_digit > 5):
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif (last_digit == 0):
    print(f"Last digit of {number} is {last_digit} and is 0")
if (last_digit < 6 and last_digit != 0):
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
