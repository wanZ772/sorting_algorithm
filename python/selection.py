# Time: O(n^2)
# Space: O(1)

from time import time
from random import randint

raw_data = []

def random_generator(target):
    for i in range(target):
        raw_data.append(randint(0, target))
def selection():
    for i in raw_data:
        point = 0
        for j in range(len(raw_data) - 1):
            if raw_data[point] > raw_data[point+1]:
                raw_data[point], raw_data[point+1] = raw_data[point+1], raw_data[point]
            point += 1
        point += 1

random_generator(10)
print(f"Raw data: {raw_data}")
start = time()
selection()
finish = time()
print(f"Sorted data: {raw_data}")
print(f"Time: {finish-start}")