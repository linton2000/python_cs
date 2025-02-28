# https://neetcode.io/problems/validate-parentheses

# First Attempt
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) % 2 != 0:
            return False

        opens = '({['
        closes = ')}]'

        for i in range(len(s)):
            target = ''
            for j in range(len(opens)):
                if s[i] == opens[j]:
                    target = closes[j]
                    break
            for k in range(i+1, len(s), 2):
                pass

# Final Solution (opened in Neetcode)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

if __name__ == '__main__':
    s = '([{}])'
    #print(isValid(s))