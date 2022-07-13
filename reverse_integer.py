class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        s=s[::-1]
        if s[len(s)-1]=='-':
            s=s[0:len(s)-1]
            x=int(s)
            x=-x
        else:
            x=int(s)
        if x >= 2**31 or x < -2**31: 
            return 0
        else:
            return x