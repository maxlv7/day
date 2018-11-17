# try except finally
# 上下文管理语句

def test():
    try:
        print("111")
        raise ImportError
        return 1
    except ImportError as e:
        print('2222')
        return 2
    else:
        print('3333')
        return 3
    finally:
        print("finally")
        # return 4

# v = test()
# print(v)


# 上下文管理协议
class Test():
    def __enter__(self):
        # 获取资源
        print("enter")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print("exit")

    def sos(self):
        print("doing~~~")


with Test() as t:
    t.sos()
