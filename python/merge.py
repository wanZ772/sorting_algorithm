from time import time
from random import randint
# raw_data = [10, 14, 28, 11, 7, 16, 30, 50]
raw_data = []
def random_generator(test_limit):
    global raw_data
    for i in range(test_limit):
        raw_data.append(randint(0, test_limit))

def merge(raw_data):
    
    if len(raw_data) > 1:
        mid = len(raw_data) // 2
        left_list = raw_data[:mid]
        right_list = raw_data[mid:]
        merge(left_list)
        merge(right_list)
        left, right, interator = 0,0,0
        
        while left < len(left_list)  and right < len(right_list):
            if left_list[left] < right_list[right]:
                raw_data[interator] = left_list[left]
                left += 1
            else:
                raw_data[interator] = right_list[right]
                right += 1
            interator += 1
        while left < len(left_list):
            raw_data[interator] = left_list[left]
            left += 1
            interator += 1
        while right < len(right_list):
            raw_data[interator] = right_list[right]
            right += 1
            interator += 1
random_generator(100000)
init_time = time()
merge(raw_data)
final_time = time() - init_time
print(raw_data)
print(f"Time: {final_time}")
