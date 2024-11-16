print('Lesson 7: Iterators, Closure function')


class Counter:
    limit: int
    index: int

    def __init__(self, limit: int):
        self.index = 0
        self.limit = limit

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        self.index += 3
        if self.index > self.limit:
            raise StopIteration
        return self.index


numbers = ['one', 'two', 3, 4, 'five', 'c++', 'c#']
counter = Counter(10)
for i in counter:
    print(numbers[i])
