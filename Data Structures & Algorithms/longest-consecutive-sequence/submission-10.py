class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        #sort the list
        sorted_list = sorted(nums)
        #store the very first number
        longest_streak = 1
        count = 1
        previous_number = sorted_list[0]
        for i in range(1, len(sorted_list)):
            current_number = sorted_list[i]

            if current_number == previous_number:
                continue

            elif current_number == previous_number + 1:
                count += 1
                previous_number = current_number

            else:
                longest_streak = max(longest_streak, count)
                count = 1
                previous_number = current_number

        return max(longest_streak, count)
            