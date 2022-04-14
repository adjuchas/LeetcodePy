from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum_lis = []
        for account in accounts:
            sum1 = 0
            for m in account:
                sum1 += m
            sum_lis.append(sum1)
        return max(sum_lis)
