class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #return max area
        maxarea = 0
        stack = [] #using monotonic stack storing pairs(index, height)

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                #while the current height is less than the previously stored height
                index, height = stack.pop()
                current_area = height * (i - index)
                #update max area
                maxarea = max(maxarea, current_area)

                start = index

            stack.append((start, h))
        #compute max height if we still have blocks in stack
        for index, height in stack:
            current_area = height * ((len(heights) - index))
            maxarea = max(current_area, maxarea)
        
        return maxarea
        