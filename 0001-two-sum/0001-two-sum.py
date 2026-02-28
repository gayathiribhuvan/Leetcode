class Solution(object):
    def twoSum(self, nums, target):
        for i in range (len(nums)):
            a = nums [i]
            b = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == b:
                    return [i,j]