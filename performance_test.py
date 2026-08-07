import time
import tracemalloc
import logging
from my_big_number import MyBigNumber

# Disable logging during performance testing for accurate CPU measurement
logging.disable(logging.CRITICAL)

calculator = MyBigNumber()

# Benchmark Workload Setup
large_number = "9" * 10_000
small_number = "1"
number_of_tests = 10

tracemalloc.start()
start_time = time.perf_counter()

for _ in range(number_of_tests):
    calculator.sum(large_number, small_number)

end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("=== PERFORMANCE TEST RESULTS ===")
print(f"Number of calculations : {number_of_tests}")
print(f"Large number length    : {len(large_number)} digits")
print(f"Small number length    : {len(small_number)} digit")
print(f"Execution time         : {end_time - start_time:.7f} seconds")
print(f"Peak memory            : {peak / (1024 * 1024):.6f} MB")