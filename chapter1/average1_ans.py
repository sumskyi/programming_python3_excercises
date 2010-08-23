#!/usr/bin/env python3

numbers = []

while True:
    try:
        line = input("enter a number or Enter to finish: ")
        if not line:
            break
        numbers.append(int(line))
    except ValueError as err:
        print(err)

count   = len(numbers)
sum     = sum(numbers)
lowest  = min(numbers)
highest = max(numbers)
mean    = sum / count

print('numbers: ', numbers)
print("count = {count} sum = {sum} lowest = {lowest} highest = {highest} mean = {mean}".format( **locals() ) )

