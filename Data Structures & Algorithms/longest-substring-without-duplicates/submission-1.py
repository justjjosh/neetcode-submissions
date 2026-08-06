class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #we are to get the longest substring without reapeating characters
        #have an edge case for an empty s:
        if not s:
            return 0
        #initialize a two pointer for a sliding window
        i, j = 0, 0

        #initialize count 
        count = 1

        #initialize a set of seen letters:
        scanned_letters = set()
        count = 0

        #we want to compare 
        while j < len(s):
            #addletters to scanned_letters
            if s[j] not in scanned_letters:
                scanned_letters.add(s[j])
                count = max(count, len(scanned_letters))
            else:
                while s[j] in scanned_letters:
                    current = len(scanned_letters)
                    count = max(current, count)
                    scanned_letters.remove(s[i])
                    i += 1
                scanned_letters.add(s[j])

            j += 1

        return count

                
                
            


        