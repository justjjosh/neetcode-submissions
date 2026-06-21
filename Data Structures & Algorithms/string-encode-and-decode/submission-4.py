class Solution:
    
    def encode(self, strs: List[str]) -> str:
        #create an empty string that we will append to and return
        result_str = ""
        for word in strs:
            result_str += f"{len(word)}#{word}"
        return result_str

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            lenght = int(s[i:j])

            word = s[j + 1: j + 1 + lenght]
            res.append(word)

            i = j+1 + lenght
            
        return res

