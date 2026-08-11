class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #have a hashmap that stores most frequently occuring
        count = {} #store the letters and their occurences
        i = 0


        res = 0
        #initialize a two pointer 
        i = 0
        #optimization
        max_freq = 0
        for j in range(len(s)):
            #get the current count of the current value we are on and increment it in count
            count[s[j]] = 1 + count.get(s[j], 0)

            #calculate current max_freq
            max_freq = max(max_freq, count[s[j]])
            #check for window validity
            while (j - i + 1) - max_freq > k:
                count[s[i]] -= 1
                i += 1

            #update res with current maximum valid window
            res = max(res, j - i + 1 )
        return res

        