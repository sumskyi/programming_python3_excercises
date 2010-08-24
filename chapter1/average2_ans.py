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
median  = '123'

def sort(seq):
    swapped = True
    while swapped:
        swapped = False
        key = 0
        for val in seq:
            if key + 1 == len(seq):
                break
            a = val
            b = seq[key+1]
            if a > b:
                seq[key] = b
                seq[key+1] = a
                swapped = True
            key += 1
    return seq

sort(numbers)

index = int(len(numbers) / 2)
median = numbers[index]
if index and index * 2 == len(numbers):
    median = (median + numbers[index - 1]) / 2


print('numbers: ', numbers)
print("count = {count} sum = {sum} lowest = {lowest} highest = {highest} mean = {mean} median = {median}".format( **locals() ) )

