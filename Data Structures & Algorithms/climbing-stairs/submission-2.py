class Solution:
    stairClimbs = {}

    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        if n in self.stairClimbs:
            return self.stairClimbs[n]
        
        self.stairClimbs[n]=self.climbStairs(n-1)+self.climbStairs(n-2)

        return self.stairClimbs[n]