from typing import List


class Solution:
    @staticmethod
    def numberOfLines(widths: List[int], s: str) -> List[int]:
        lis = []
        first = ord('a')
        last = ord('z')
        for i in range(first, last+1):
            lis.append(chr(i))
        dic = dict(zip(lis, widths))
        all_widths = 0
        for i in s:
            if (all_widths + dic[i]) % 100 < dic[i] and (all_widths + dic[i]) % 100 != 0:
                all_widths = (all_widths // 100 + 1) * 100 + dic[i]
            else:
                all_widths += dic[i]
        if all_widths % 100 > 0:
            return [all_widths // 100 + 1, all_widths % 100]
        else:
            return [all_widths // 100, 100]
