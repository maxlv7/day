from collections import abc

import abc
# + += extend append
a = [1,2]
b = [3,4]

a+=(1,3)

# 这里其实内部调用了__iadd__方法
# a = a+(1,3)
print(a)
