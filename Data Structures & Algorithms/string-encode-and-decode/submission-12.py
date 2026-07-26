class Solution:
    
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        if strs == []:
            encoded_str = "🫥"
        for i in range(len(strs)):
            if i == len(strs) - 1:
                encoded_str += strs[i]
            else:
                encoded_str += strs[i] + "😄"
        return encoded_str

    def decode(self, encoded_str: str) -> list:
        if encoded_str == "🫥":
            return []
        return encoded_str.split("😄")
