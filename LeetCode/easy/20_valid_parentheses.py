# https://leetcode.com/problems/valid-parentheses/

OPENING_BRACKETS = ['(', '[', '{']
CLOSING_BRACKETS = [')', ']', '}']


"""Stack-based solution."""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in OPENING_BRACKETS:
                stack.append(char)
            else:
                if not stack: # stack is empty
                    return False

                popped = stack.pop()
                if(CLOSING_BRACKETS.index(char) != OPENING_BRACKETS.index(popped)):
                    return False

        if len(stack) != 0:
            return False

        return True
