# This solution is the best one because it iterates through the list only once, making it a Big O(n) algorithm.
class Solution:
    def twoSum(nums, target):
        hash = {}
        for idx, i in enumerate(nums):
            # If the number that we stored is in the hash, you are going to return the index of the number and the index of the current number
            if i in hash:
                return [hash[i], idx]
            else:
                # If the number is not in the hash, keep the difference of the target - the current number in the hash,
                # and the index so when you find the result, you can return it.
                hash[target - i] = idx
        


    print(twoSum([2, 7, 11, 15], 9))