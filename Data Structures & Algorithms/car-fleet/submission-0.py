class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #map each car's positon to it's speed
        cars = list(zip(position, speed))
        #sort the cars
        cars.sort()
        #sort in descending order
        cars.reverse()
        #create a stark that keeps track of only time greater than previous time
        stack = []
        for i in range(len(cars)):
            #calculate time:
            current_time = (target - cars[i][0]) / cars[i][1]
            if not stack:
                stack.append(current_time)
            else:
                if current_time <= stack[-1]:
                    continue
                else:
                    stack.append(current_time)
        return len(stack)
                