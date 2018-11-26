from collections.abc import Iterable,Iterator

a = [1,2,3]


ii = iter(a)
print(isinstance(a,Iterable))
print(isinstance(a,Iterator))