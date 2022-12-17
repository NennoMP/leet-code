# https://leetcode.com/problems/length-of-last-word/


"Two-pointer based solution."
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0

        prev = ' '
        for char in s:
            # Start of a new word
            if char != ' ' and prev == ' ':
                result = 1
            # Not a new word
            elif char != ' ':
                result += 1
            prev = char

        return result