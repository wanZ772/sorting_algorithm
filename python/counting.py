# time : O(n^2)
# Space: O(1)

from time import time
from random import randint

raw_data = []
def random_generator(target):
    for i in range(target):
        raw_data.append(randint(0, target))

def counting(data):
    maxx = max(data)
    counts = [0] * (maxx+1)
    for i in data:
        counts[i] += 1
    
    j = 0
    for i in range(maxx + 1):
        while counts[i] > 0:
            data[j] = i
            j += 1
            counts[i] -= 1
            # j += 1
        
    return data

random_generator(100)
print(f"Raw data: {raw_data}")
start = time()
sorted_ = counting(raw_data)
finish = time()
print(f"Sorted data: {sorted_}")
print(f"Time: {finish-start}")