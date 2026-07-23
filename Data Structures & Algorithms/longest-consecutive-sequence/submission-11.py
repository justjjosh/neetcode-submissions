class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Convert the list to a Hash Set for instant O(1) lookups
        num_set = set(nums)
        longest_streak = 0

        # We iterate through the SET, not the list (removes duplicates instantly!)
        for num in num_set:
            # Check if this number is the START of a sequence.
            # It is only a start if the number before it does NOT exist.
            if (num - 1) not in num_set:
                
                # We found a starting number! Let's start counting.
                current_num = num
                current_streak = 1

                # Keep checking if the next consecutive number exists in our set
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                # The chain broke. Update the high score!
                longest_streak = max(longest_streak, current_streak)

        return longest_streak