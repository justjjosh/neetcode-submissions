class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        open_brac = []
        for char in s:
            if char not in bracket_map:
                open_brac.append(char)
            else:
                if not open_brac:
                    return False
                last_seen = open_brac[len(open_brac) - 1]
                if bracket_map[char] != last_seen:
                    return False
                else:
                    open_brac.pop()

        return open_brac == []



