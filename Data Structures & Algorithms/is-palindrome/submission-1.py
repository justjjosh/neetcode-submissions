class Solution:
    def isPalindrome(self, s: str) -> bool:
        #i want to have a left and right pointer
        L = 0
        R = len(s) - 1
        #check for edge cases- a while loop
        while R > L:
            if not s[L].isalnum():
                L += 1
            elif not s[R].isalnum():
                R -= 1
            elif s[L].lower() != s[R].lower():
                    return False
            else:
                L += 1
                R -= 1
        return True
        