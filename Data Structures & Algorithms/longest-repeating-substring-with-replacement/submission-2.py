class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #have a hashmap that stores most frequently occuring
        count = {}

        res = 0
        #initialize a two pointer 
        i = 0
        for j in range(len(s)):
            #get the current count of the current value we are on and increment it in count
            count[s[j]] = 1 + count.get(s[j], 0)
            #check for window validity
            while (j - i + 1) - max(count.values()) > k:
                count[s[i]] -= 1
                i += 1

            #update res with current maximum valid window
            res = max(res, j - i + 1 )
        return res

        