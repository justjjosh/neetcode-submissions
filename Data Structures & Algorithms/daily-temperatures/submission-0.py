class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #return an array the lenght of input
        res = [0] * len(temperatures)
        stack = []
        #loop through index, and values
        for i, value in enumerate(temperatures):
            #while loop that computes the numbers of days ahead for hotter temp
            while stack and temperatures[i] > temperatures[stack[-1]]:
                days_back = stack[-1]
                days_ahead = i - days_back
                res[days_back] = days_ahead
                stack.pop()

            stack.append(i)
        return res

                

        