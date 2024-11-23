# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
#
# A shift on s consists of moving the leftmost character of s to the rightmost position.
#
# For example, if s = "abcde", then it will be "bcdea" after one shift.
#

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        doubled_s = s + s
        return goal in doubled_s