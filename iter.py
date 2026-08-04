class num:
    def __init__(self, count):
        self.count = count
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.count:
            self.i += 1
            return self.i
        else:
            raise StopIteration


for i in num(10):
    print(i)
