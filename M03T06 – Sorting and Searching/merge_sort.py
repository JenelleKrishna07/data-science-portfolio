# merge_sort.py

def merge_sort_by_length(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_by_length(arr[:mid])
    right = merge_sort_by_length(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if len(left[0]) > len(right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left + right)
    return result

# Test lists
list1 = ["pineapple", "fig", "banana", "apple", "coconut", "peach", "kiwi", "grapefruit", "mango", "papaya"]
list2 = ["elephant", "dog", "rhinoceros", "cat", "giraffe", "lion", "tiger", "hippo", "zebra", "cheetah"]
list3 = ["strawberry", "raspberry", "blueberry", "blackberry", "cranberry", "grape", "pear", "plum", "nectarine", "apricot"]

# Apply sorting
print(merge_sort_by_length(list1))
print(merge_sort_by_length(list2))
print(merge_sort_by_length(list3))
