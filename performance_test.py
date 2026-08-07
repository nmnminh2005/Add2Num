import time
import tracemalloc

from my_big_number import MyBigNumber


# Create the calculator
calculator = MyBigNumber()

# Test data
large_number = "9" * 10_000
small_number = "1"

# Number of repetitions
number_of_tests = 10


# Start memory measurement
tracemalloc.start()

# Start timer
start_time = time.perf_counter()


# Run the addition repeatedly
for _ in range(number_of_tests):
    calculator.sum(large_number, small_number)


# Stop timer
end_time = time.perf_counter()


# Get memory usage
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()


# Calculate results
execution_time = end_time - start_time
peak_memory = peak / (1024 * 1024)


# Display results
print("=== PERFORMANCE TEST ===")
print("Number of calculations:", number_of_tests)
print("Large number digits:", len(large_number))
print("Small number digits:", len(small_number))
print("Execution time:", execution_time, "seconds")
