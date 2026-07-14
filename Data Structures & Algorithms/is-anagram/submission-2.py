class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #sort both strings and then compare the sorted string
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        if sorted_s == sorted_t:
            return True
        else:
            return False