from time import time
from random import randint


raw_data = []

def random_generator(test_limit):
    for i in range(0, test_limit):
        raw_data.append(randint(0, test_limit))

def bubble():
    for i in raw_data:
        for j in range(len(raw_data) - 1):
            if raw_data[j] > raw_data[j+1]:
                raw_data[j], raw_data[j+1] = raw_data[j+1], raw_data[j]
    return raw_data


random_generator(1000)
print(f"Unsorted: {raw_data}")
start_time = time()
sorted_data = bubble()
end_time = time() - start_time
print(f"sorted: {sorted_data}")
print(f"Time: {end_time}")