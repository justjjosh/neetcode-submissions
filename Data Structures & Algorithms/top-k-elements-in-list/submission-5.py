class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #store each number and keep count
        number_count = {}
        for number in nums:
            if number in number_count:
                number_count[number] += 1
            else:
                number_count[number] = 1

        sorted_dict = sorted(number_count.items(), key=lambda item: item[1], reverse=True)
        
        return [key for key, value in sorted_dict[:k]]