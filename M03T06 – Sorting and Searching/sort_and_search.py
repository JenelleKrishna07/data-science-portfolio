# sort_and_search.py

# Linear Search
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

# Insertion Sort
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

# Binary Search
def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example list
data = [12, 4, 9, 1, 7, 3, 15, 2, 6, 5]

# Step 1: Linear search
print("Linear Search index:", linear_search(data, 9))  # O(n)

# Step 2: Insertion sort
sorted_data = insertion_sort(data.copy())
print("Sorted list:", sorted_data)  # O(n^2)

# Step 3: Binary search
print("Binary Search index:", binary_search(sorted_data, 9))  # O(log n)
