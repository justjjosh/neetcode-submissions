class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_count = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in word_count:
                word_count[sorted_word].append(word)
            else:
                word_count[sorted_word] = [word]

        return list(word_count.values())

