# O (Log N)

def search(nums, target):
    lo = 0
    hi = len(nums)
    while lo < hi:
        mid = int(lo+hi) // 2
        if nums[mid] == target:
            return mid 
        elif nums[mid] > target:
            hi = mid 
        elif nums[mid] < target:
                lo = mid + 1
    return -1

print(search([-1,0,3,5,9,12], 9 ))