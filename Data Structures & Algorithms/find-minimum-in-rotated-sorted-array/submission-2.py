class Solution:
    def findMin(self, nums: List[int]) -> int:
        #let's have a left and right pointer
        l, r = 0, len(nums) - 1
        
        while l < r:
            #find the middle ground
            m = int((l + r) / 2)
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]


        