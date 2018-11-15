# python魔法函数

class Company():
    def __init__(self,employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

    def __str__(self):
        return ",".join(self.employee)

cpy = Company(["li","yyx"])

print(cpy)

