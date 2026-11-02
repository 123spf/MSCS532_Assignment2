import time
import tracemalloc
import random

# ==========================================
# 1. Merge Sort Implementation
# ==========================================
def merge_sort(arr):
    """
    Recursively sorts an array using the divide-and-conquer Merge Sort algorithm.
    Time Complexity: Theta(n lg n) across all cases.
    Space Complexity: O(n) auxiliary memory for temporary arrays.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)

def merge(left, right):
    """Helper function to merge two sorted lists into a single sorted list."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
# ==========================================
# 2. Binary Search Implementation
# ==========================================
def binary_search(arr, target):
    """
    Searches for a target value in a sorted array using divide and conquer.
    Time Complexity: O(lg n) worst/average case, Omega(1) best case.
    Note: The input array MUST be sorted beforehand; otherwise, it returns -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1


# ==========================================
# 3. Performance Testing & Metrics
# ==========================================
def run_tests():
    n = 10000
    print(f"Generating test datasets of size n = {n}...\n")

    random_data = [random.randint(1, 100000) for _ in range(n)]
    sorted_data = sorted(random_data)
    reverse_sorted_data = sorted(random_data, reverse=True)

    datasets = {
        "Random Data": random_data,
        "Sorted Data": sorted_data,
        "Reverse-Sorted Data": reverse_sorted_data
    }

    print("--- MERGE SORT PERFORMANCE ---")
    for name, data in datasets.items():
        test_copy = list(data)

        tracemalloc.start()
        start_time = time.perf_counter()
        
        sorted_result = merge_sort(test_copy)
        
        end_time = time.perf_counter()
        current_mem, peak_mem = tracemalloc.get_tracemalloc_memory()
        tracemalloc.stop()

        elapsed_ms = (end_time - start_time) * 1000
        print(f"[{name}] Time: {elapsed_ms:.4f} ms | Peak Memory: {peak_mem / 1024:.2f} KB")

    print("\n--- BINARY SEARCH PERFORMANCE ---")
    target_value = sorted_data[len(sorted_data) // 2]

    for name, data in datasets.items():
        # Sort beforehand to satisfy Binary Search's operational requirement
        if name == "Reverse-Sorted Data":
            active_data = sorted(data) 
        else:
            active_data = data

        start_time = time.perf_counter()
        index = binary_search(active_data, target_value)
        end_time = time.perf_counter()

        elapsed_ns = (end_time - start_time) * 1_000_000
        print(f"[{name}] Found target at index {index} | Time: {elapsed_ns:.4f} microseconds")

if __name__ == "__main__":
    run_tests()

