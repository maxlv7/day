class Date():
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    # @staticmethod
    # def parse_str(date_str):
    #     y, m, d = tuple(date_str.split('-'))
    #     return Date(int(y),int(m),int(d))
    #
    #
    # @classmethod
    # def pars_str(cls,str):
    #     y, m, d = tuple(date_str.split('-'))
    #     return cls(int(y), int(m), int(d))
    # def __str__(self):
    #     return "{year}/{month}/{day}".format(year=self.year,month=self.month,day=self.day)


if __name__ == '__main__':
    new_day = Date(2018,11,6)
    print(new_day)

    #使用静态方法
    date_str = "2018-5-5"
    print(Date.parse_str(date_str))

    #使用类方法
    print(Date.pars_str(date_str))
