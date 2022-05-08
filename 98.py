from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        lis = [n for n in range(0, len(s))]
        ans = []
        for i in s:
            if i == 'I':
                ans.append(lis.pop(0))
            else:
                ans.append(lis.pop())
        ans.append(lis[0])
        return ans
