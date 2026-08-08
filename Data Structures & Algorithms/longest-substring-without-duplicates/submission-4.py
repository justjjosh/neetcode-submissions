class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #we are to get the longest substring without reapeating characters
        j = 0

        #initialize a set of seen letters:
        scanned_letters = set()

        #initialize count 
        res = 0

        for i in range(len(s)):
            #while a duplicate exists in our scanned letters
            while s[i] in scanned_letters:
                scanned_letters.remove(s[j])
                j += 1
            scanned_letters.add(s[i])

            res = max(res,  i - j + 1)

        return res

                
                
            


        