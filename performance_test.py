# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 22:45:30 2026

@author: Owner
"""


import time
import tracemalloc

from my_big_number import MyBigNumber


calculator = MyBigNumber()

large_number = "9" * 1_000_000
small_number = "1"

number_of_tests = 1_000_000

tracemalloc.start()

start_time = time.perf_counter()

for _ in range(number_of_tests):
    calculator.sum(large_number, small_number)

end_time = time.perf_counter()

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

execution_time = end_time - start_time
peak_memory = peak / (1024 * 1024)

print("Number of calculations:", number_of_tests)
print("Large number digits:", len(large_number))
print("Small number digits:", len(small_number))
print("Execution time:", execution_time, "seconds")
print("Peak memory:", peak_memory, "MB")