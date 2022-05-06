class RecentCounter:

    def __init__(self):
        self.biggest = 0
        self.lis = []

    def ping(self, t: int) -> int:
        self.lis.append(t)
        while self.lis[0] < t - 3000:
            self.lis.pop(0)
        return len(self.lis)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
