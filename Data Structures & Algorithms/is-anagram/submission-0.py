class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #do they have the exact number of characters
        #have hashmaps to store letter and count
        count_s = {}
        count_t = {}
        if len(s) != len(t):
            return False
        for letter in s:
            if letter in count_s:
                count_s[letter] += 1
            else:
                count_s[letter] = 1

        for letter in t:
            if letter in count_t:
                count_t[letter] += 1
            else:
                count_t[letter] = 1
        return count_s == count_t
        