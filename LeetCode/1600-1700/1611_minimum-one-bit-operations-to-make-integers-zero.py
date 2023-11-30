class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        
        k = 0
        curr = 1
        while (curr * 2) <= n:
            curr *= 2
            k += 1

        return 2 ** (k + 1) - 1 - self.minimumOneBitOperations(n ^ curr)        


# "In binary representation, each position is referred to as a bit. The bits are numbered from right to left starting from 0. So, the “0th bit” refers to the rightmost bit, and the “1st bit” refers to the second bit from the right."

# For example, in the binary number “1101”:

# The 0th bit is 1 (the rightmost bit)
# The 1st bit is 0
# The 2nd bit is 1
# The 3rd bit is 1 (the leftmost bit)

# And also the phrase "(i-2)th through 0th bits are set to 0" means that every bit position from the (i-2)th bit position to the 0th bit position is set to 0.

# The description of the two operations can be rephrased as,

# Op1: Invert the 0th bit
# Op2: Invert the ith bit, only if (i-1)th bit is set to 1, and if there are bits from (i-2) to 0, all of them are 0 already.

# Looking at the given two test cases with this,

# Given test case 1:

# 11

# 01 (we get this using Op2, inverting bit at i = 1, as (i-1)th bit is 1 and there are no bits from (i-2) to 0)
# 00 (we get this using Op1, inverting 0th bit)

# 2 operations needed - Op2, Op1

# Given test case 2:

# 110

# 010 (we get this using Op2, inverting bit at i = 2, as (i-1)th bit is 1 and bits from (i-2) to 0 are all 0)
# 011 (we get this using Op1, inverting 0th bit)
# 001 (we get this using Op2, inverting bit at i = 1, as (i-1)th bit is 1 and there are no bits from (i-2) to 0)
# 000 (we get this using Op1, inverting 0th bit)

# 4 operations needed - Op2, Op1, Op2, Op1
