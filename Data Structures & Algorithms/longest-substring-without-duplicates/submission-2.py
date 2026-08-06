class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #we are to get the longest substring without reapeating characters
        #have an edge case for an empty s:
        if not s:
            return 0
        #initialize a two pointer for a sliding window
        i, j = 0, 0

        #initialize count 
        res = 0

        #initialize a set of seen letters:
        scanned_letters = set()
        count = 0

        while j < len(s):
            #addletters to scanned_letters
            if s[j] not in scanned_letters:
                scanned_letters.add(s[j])
            else:
                #strip off all the previous letter until s[j] is no longer in scanned_letters
                while s[j] in scanned_letters:
                    scanned_letters.remove(s[i])
                    i += 1
                scanned_letters.add(s[j])
            res = max(res, j - i + 1)

            j += 1

        return res

                
                
            


        