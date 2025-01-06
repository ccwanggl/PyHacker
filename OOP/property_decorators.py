class Employee:
    number_of_employees = 0
    raise_amount = 1.04
    def __init__(self, first, last ,pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.number_of_employees += 1

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleting fullname')
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Smith', 50000)

print(emp_1.first)
emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)

# @property 装饰器将方法转换为属性
print(emp_1.fullname)

emp_1.fullname = 'Guoliang WANG'

isinstance(emp_1, Employee)
del emp_1.fullname