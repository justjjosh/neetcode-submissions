class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #i and j are unique
        #we need both the index and value
        #store both the index and its values
        found_numbers = {}
        for index, value in enumerate(nums):
            compliment = target - value
            if compliment in found_numbers:
                return [found_numbers[compliment], index]
            else:
                found_numbers[value] = index
