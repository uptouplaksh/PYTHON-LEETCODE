# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer num, return its complement.
class Solution:
    def findComplement(self, num: int) -> int:
        num_binary = format(num, 'b')
        complement = ''
        for val in num_binary:
            if val == '0':
                complement += '1'
            else:
                complement += '0'
        return int(complement, 2)