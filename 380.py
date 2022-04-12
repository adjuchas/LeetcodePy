import random


class RandomizedSet:

    def __init__(self):
        self.lis = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        if val not in self.dic.keys():
            self.dic[val] = len(self.lis)
            self.lis.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.dic.keys():
            ind = self.dic[val]
            self.lis[ind] = self.lis[-1]
            self.dic[self.lis[ind]] = ind
            self.lis.pop()
            self.dic.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.lis)
# choice 是需要导入random包

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()