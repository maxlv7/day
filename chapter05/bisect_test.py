import bisect

# 用来处理已排序的序列，用来维持已排序的序列
# 二分查找

inter_list = []
bisect.insort(inter_list,3)
bisect.insort(inter_list,5)
bisect.insort(inter_list,7)
bisect.insort(inter_list,4)
bisect.insort(inter_list,9)

print(inter_list)