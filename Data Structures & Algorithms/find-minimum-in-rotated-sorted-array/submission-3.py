class Solution:
    def findMin(self, nums: List[int]) -> int:
        #initialize two pointers
        l, r = 0, len(nums) - 1
        while l < r:
            #get the middle index
            m = (r + l) // 2
            #get all the values
            left, middle, right = nums[l], nums[m], nums[r]

            #condition for spliting the array in half
            if middle > right:
                l = m + 1
            else:
                r = m

        return nums[l]


     
        


        