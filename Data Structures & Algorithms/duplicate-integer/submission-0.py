class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #we must have everything in the array to be unique
        found_numbers = set()
        #loop and check through the numbers
        for num in nums:
            if num in found_numbers:
                return True
            else:
                found_numbers.add(num)
        return False
        