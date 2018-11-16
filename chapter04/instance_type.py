class A:
    pass


class B(A):
    pass

b = B()

print(isinstance(b,B))
print(isinstance(b,A))
#is 就是判断id是否一样
print(type(b) is B)
