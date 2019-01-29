from typing import List


def test():
    i = 123
    yield i
    i += 1


f = test()
a = f.send(None)
print(a)
