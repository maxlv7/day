# 列表生成式 性能高于列表操作

odd_list = [ i*i for i in range(21) if i%2==1 ]
print(odd_list)

# 生成器表达式

odd_list1 = ( i*i for i in range(21) if i%2==1 )

# 字典推导式

my_names = {'li':20,'yyx':21,'lxh':20}
r_my_name = {value:key for key,value in my_names.items()}
print(r_my_name)

# 集合推导式

my_set = {k for k,v in my_names.items()}
print(type(my_set))
print(my_set)