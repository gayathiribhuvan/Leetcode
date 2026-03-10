class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        num = 0
        sign = 1
        n = len(s)

        while i < n and s[i] == " ":
            i += 1

        if i < n and (s[i] == "+" or s[i] == "-") :
            if s[i] == "-":
                sign = -1
            i += 1
        
        while i < n and s[i].isdigit():
            num = num*10 + int(s[i])
            i += 1
        num *= sign

        low = -2**31
        high = 2**31 - 1

        if num < low:
            return low
        elif num > high:
            return high
        return num     