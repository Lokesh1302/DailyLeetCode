class Solution:
    def pivotInteger(self, n: int) -> int:
        low, high = 1, n

        while low <= high:
            mid = low + (high - low) // 2
            left_sum = (mid - 1) * (mid) // 2
            right_sum = (n - mid) * (n + mid + 1) // 2
            # print(mid, left_sum, right_sum)
            if left_sum == right_sum:
                return mid
            
            elif left_sum > right_sum:
                high = mid - 1
            else:
                low = mid + 1
        return -1


# The formula for the sum of an arithmetic series is:

# S = (N / 2) * (A1 + An)

# where:

# S is the sum of the series.
# N is the number of terms in the series.
# A1 is the first term of the series.
# An is the last term of the series.


# Given mid as the midpoint:

# For LEFT SUM =

# N = mid − 1 (number of terms)
# A1 = 1 (first term)
# An = mid - 1 (last term)


# For RIGHT SUM =

# N = n - (mid + 1) + 1  = n - mid (number of terms)
# A1 = mid + 1 (first term)
# An = N (last term)
