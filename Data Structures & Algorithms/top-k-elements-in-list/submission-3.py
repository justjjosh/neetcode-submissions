class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        found_numbers = {}
        for number in nums:
            if number in found_numbers:
                found_numbers[number] += 1
            else:
                found_numbers[number] = 1
        sorted_values = sorted(found_numbers.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_values[:k]]