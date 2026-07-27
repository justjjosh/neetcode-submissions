class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #we want to have a left and right pointer
        #get our current height
        #calculate the width
        #calculate the current area
        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            #get the height and width
            height = min(heights[l], heights[r])
            width = r - l
            #calculate the area
            current_area = height * width
            #set the maximum area
            max_area = max(max_area, current_area) 

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area


        