class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #we must have everything in the array to be unique
        found_numbers = set()
        for number in nums:
            if number in found_numbers:
                return True
            else:
                found_numbers.add(number)
        return False