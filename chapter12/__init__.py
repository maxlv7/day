class Test():
    def route(self, rule):
        def decorator(f):
            # endpoint = options.pop('endpoint', None)
            # self.add_url_rule(rule, endpoint, f, **options)\
            # print(f.__name__)
            def wrapper(a):
                return f(a)
            return wrapper

        return decorator

    def my(self, rule):
        def decorator(f):
            print(f.__name__)
            print(rule)
            return f

        return decorator


t = Test()


@t.route('/')
def test1(a):
    print(1+a)
    return "test111"


# @t.my('/n')
# def test2():
#     print(1)
#     return "test2"


(test1(3))
print('===========')
# print(test2())
