array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


target = 9

def binary_search(array, target):
    low = 0
    high = len(array) - 1
    center = (low + high) // 2

    while low <= high:
        center = (high + low) // 2

        if array[center] == target:
            return array[center - 1]
        if array[center] < target:
            low = center + 1
            continue
        if array[center] > target:
            high = center - 1
            continue
        
print(binary_search(array, target))
