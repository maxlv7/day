# 一个经典的错误
# is用来判断是否是同一个对象 id是否相同

def add(a,b):
    # 会把原来的也修改了(list dict)
    a+=b
    return a

if __name__ == '__main__':
    a = 1
    b =2
    c = add(a,b)
    # print(a,b,c)

    a = [1,2]
    b = [3,4]
    d = add(a,b)
    print(d)
    print(a)
    print(b)