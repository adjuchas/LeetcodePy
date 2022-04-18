from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        lis = [i for i in range(1, n+1)]
        lis1 = sorted(list(map(str, lis)))
        lis2 = list(map(int, lis1))
        return lis2
