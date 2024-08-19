# Time: O(n log n)
# Space: O(log2n)

from random import randint
from time import time

def random_generator(target):
    raw_data = []
    for i in range(target):
        raw_data.append(randint(0, target))
    return raw_data

def merge(data):
    n = len(data)

    if n == 1:
        return data
    else:
        mid = n // 2
        left = data[:mid]
        right = data[mid:]

        left = merge(left)
        right = merge(right)

        left_point, right_point, left_length, right_length = 0,0,len(left),len(right)

        sorted_data = []

        while left_point < left_length and right_point < right_length:
            if left[left_point] < right[right_point]:
                sorted_data.append(left[left_point])
                left_point += 1
            else:
                sorted_data.append(right[right_point])
                right_point += 1
        while left_point < left_length:
            sorted_data.append(left[left_point])
            left_point += 1
        while right_point < right_length:
            sorted_data.append(right[right_point])
            right_point += 1

        return sorted_data


unsorted_data = random_generator(20)
# print(f"Raw Data: {unsorted_data}")
start = time()
sorted_ = merge(unsorted_data)
finish = time() - start
print(f"Sorted Data: {sorted_}")
print(f"Total time: {finish}")