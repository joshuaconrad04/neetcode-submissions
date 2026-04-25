class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        s = []

        for c in asteroids:
            while s and c<0 and s[-1] > 0:
                if abs(c)>abs(s[-1]):
                    s.pop()
                elif abs(c)<abs(s[-1]):
                   c=0
                else:
                    s.pop()
                    c=0
            if c!=0:
                s.append(c)
        return s 
