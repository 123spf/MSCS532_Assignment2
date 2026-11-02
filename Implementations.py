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

