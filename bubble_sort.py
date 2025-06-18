
import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def generate_test_data(size, data_type="random"):
    if data_type == "random":
        return [random.randint(0, size * 10) for _ in range(size)]
    elif data_type == "partially_sorted":
        arr = [random.randint(0, size * 10) for _ in range(size)]
        # Sort a portion to make it partially sorted
        arr[:size//2] = sorted(arr[:size//2])
        return arr
    elif data_type == "reverse_order":
        return list(range(size, 0, -1))
    else:
        raise ValueError("Invalid data_type. Choose from 'random', 'partially_sorted', 'reverse_order'.")

def measure_execution_time(algorithm, arr):
    start_time = time.perf_counter_ns()
    algorithm(arr.copy())
    end_time = time.perf_counter_ns()
    return (end_time - start_time) / 1_000_000 # Convert to milliseconds

if __name__ == "__main__":
    sizes = [10, 100, 1000, 5000, 10000, 50000, 100000]
    data_types = ["random", "partially_sorted", "reverse_order"]
    algorithm = bubble_sort
    algo_name = "Bubble Sort"
    num_runs = 5

    print(f"--- {algo_name} Execution Times (ms) ---")
    for size_value in sizes:
        print(f"\nSize: {size_value} elements")
        for d_type in data_types:
            times = []
            for _ in range(num_runs):
                data = generate_test_data(size_value, d_type)
                time_taken = measure_execution_time(algorithm, data)
                times.append(time_taken)
            avg_time = sum(times) / num_runs
            print(f"  Data Type: {d_type}: {avg_time:.4f} ms")


