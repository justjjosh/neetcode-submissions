class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #i and j are unique
        #find the index i.e store numbers with their indicies
        found_numbers={}
        for index, value in enumerate(nums):
            compliment = target - value
            if compliment in found_numbers:
                return[found_numbers[compliment], index]
            found_numbers[value] = index