class Solution:
    def integerBreak(self, n: int) -> int:
        # 贪心算法：假设商为 k = n // 3, 余数 r = n % 3
        # if r = 0, res = 3 ** k
        # if r = 1, res = 3 ** (k-1) * 4
        # if r = 2, res = 3 ** (k) * 2
        if n <= 3: return n -1 
        remain = n % 3
        k = n // 3
        if remain == 0:
            return 3 ** k
        elif remain == 1:
            return 3 ** (k - 1) * 4
        elif remain == 2:
            return 3 ** (k) * 2
        
            