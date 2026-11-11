class Solution:
    def __init__(self):
        self.countSteps = {}

    def climbStairs(self, n: int) -> int:
        # Your solution here
        if n==1:
            return 1
        if n==2:
            return 2
        
        if n in self.countSteps:
            return self.countSteps[n]

        self.countSteps[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.countSteps[n]