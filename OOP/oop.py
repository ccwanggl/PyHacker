class Employee:
    number_of_employees = 0
    raise_amount = 1.04
    def __init__(self, first, last ,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.number_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User',60000)

print(emp_1.raise_amount)
print(Employee.raise_amount)

print('----------------->')

print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employee.__dict__)

emp_1.raise_amount = 1.05

print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.number_of_employees)