class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        for e in s:
            if e in mp:
                if stack and stack[-1] == mp[e]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(e)
        return len(stack) == 0