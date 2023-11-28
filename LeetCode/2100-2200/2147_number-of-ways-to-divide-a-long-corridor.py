class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 1_000_000_007

        zero = 0
        one = 0
        two = 1

        for thing in corridor:
            if thing == "S":
                zero = one
                one, two = two, one
            else:
                two = (two + zero) % MOD

        return zero  
