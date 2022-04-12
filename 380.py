import random


class RandomizedSet:

    def __init__(self):
        self.lis = []   # 数组通过len（）用来充当字典中的值，也可以用来返回一个随机值choice()
        self.dic = {}   # 字典实现哈希表，可以在O(1)时间内找到是否存在和删除

    def insert(self, val: int) -> bool:
        if val not in self.dic.keys():
            self.dic[val] = len(self.lis)
            self.lis.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.dic.keys():
            ind = self.dic[val]
            self.lis[ind] = self.lis[-1]    # 先换位置，再pop，保证也是O(1)内删除
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