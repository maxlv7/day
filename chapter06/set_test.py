# set 集合 frozenset不可变集合 无序

s = set('abcdedd')
# print(s)
s.add('test')
# print(s)

b = frozenset("abcde")
# print(hash(b))
# print(b.__hash__())

# set添加数据


one = set("abc")
two = set("degabc")

# 差集
a = one.difference(two)
print(a)
print(one-two)
print(one|two)
print(one&two)

print(one.issubset(two))