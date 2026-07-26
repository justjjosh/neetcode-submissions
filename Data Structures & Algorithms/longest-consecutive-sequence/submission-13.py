class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Convert the list to a Hash Set for instant O(1) lookups
        #we need a hash set
        num_set = set(nums)
        longest_streak = 0
        for number in num_set:
            if number - 1 not in num_set:
                current_number = number
                current_streak = 1
                while(current_number + 1) in num_set:
                    current_streak += 1
                    current_number += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak

















