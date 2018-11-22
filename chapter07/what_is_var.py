# python中的变量其实就是一个指针

a = [1,2,3]
b = a
b.append(4)
print(a)
# 判断是否是同一个对象
print(a is b)

m = 1
n = 1
print(m is n)
print(m==n)
# __eq__
print(m.__eq__(n))