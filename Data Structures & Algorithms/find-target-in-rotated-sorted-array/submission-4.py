class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #initialize our pointers
        l, r = 0, len(nums)-1
        while l <= r:
            #middle
            m = (r + l) // 2
            #get our values
            left, middle, right = nums[l], nums[m], nums[r]

            #check if our target is the middle value
            if target == middle:
                return m

            #check for valid sorted
            #compare mid to left and get validity of left sorted
            if middle >= left:
                if left <= target < middle:
                    r = m - 1
                else:
                    l = m + 1
            #outer else block that checks the validity of the right sorted
            else:
                #range = left to middle to right
                if middle < target <= right:
                    l = m + 1
                else:
                    r = m - 1

        return -1


