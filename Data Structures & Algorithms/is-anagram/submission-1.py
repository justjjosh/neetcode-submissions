class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #sort both strings
        if len(s) != len(t):
            return False
        new_s = "".join(sorted(s))
        new_t = "".join(sorted(t))
        return new_s == new_t
        