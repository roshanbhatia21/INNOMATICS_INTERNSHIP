class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a=x^y
        setbits=0
        while(a>0):
            setbits+=a&1
            a>>=1
        return  setbits   
            