class Person(object):
    def __new__(cls, *args, **kwargs):
        print("new")
        return super().__new__(cls)

    def __init__(self):
        print("init")


if __name__ == '__main__':
    Person()