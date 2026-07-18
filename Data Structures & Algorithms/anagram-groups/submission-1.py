class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create an empty dictionary
        #store the first sorted word as the key of the dict and then append every word that fits to the list
        #return the list
        word_count = {}
        
        # 2. Walk through the array exactly one time (No nested loops!)
        for word in strs:
            sorted_word = "".join(sorted(word))
            
            if sorted_word in word_count:
                word_count[sorted_word].append(word)
            else:
                word_count[sorted_word] = [word]
        return list(word_count.values())
                
