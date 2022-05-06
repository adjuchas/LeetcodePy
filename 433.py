from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        else:
            deque = [(start, 0)]
            while deque:
                str1, count = deque.pop(0)
                for index, char in enumerate(str1):
                    for i in "ACGT":
                        if char != i:
                            new_node = str1[:index] + i + str1[index+1:]
                            if new_node == end:
                                return count + 1
                            elif new_node not in bank:
                                pass
                            else:
                                deque.append((new_node, count+1))
                                bank.remove(new_node)
            return -1
