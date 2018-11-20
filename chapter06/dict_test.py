# dict常用方法

a = dict()
a["li"] = 20
a["li2"] = 22
# clear
b = a.copy()
b['li3'] = 23

c = [1,2,3]

d = dict.fromkeys(c,"test")

# 比较重要的方法
d.setdefault(4,"test4")
print(d)

d.update({'test5':5})
d.update([('test6',6)])

print(d)
