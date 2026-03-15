class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        res = []
        if len(s) <= 1:
            return False
        for i in s:
            if i == "(" or i =="[" or i == "{":
                stack.append(i)
            elif len(stack) == 0 and (i == ")" or i == "}" or i == "]"):
                return False
            else:
                if i == ")" and stack[-1] == "(":
                    res.append(True)
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    res.append(True)
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    res.append(True)
                    stack.pop()
                else:
                    res.append(False)
        if False in res or len(stack) != 0:
            return False
        else:
            return True            