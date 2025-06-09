class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
         res =sorted(str(i)for i in range(1,n+1))[k-1]
         return int(res)
        