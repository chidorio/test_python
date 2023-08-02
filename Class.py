# class Shape:
#
#     def what_am_i(self):
#         print('Я - фигура.')
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def calculate_perimeter(self):
#         area = self.a + self.b + self.c
#         return area
#
#
# class Square(Shape):
#     square_list = []
#
#     def __init__(self, a):
#         self.a = a
#         self.square_list.append(self)
#
#     def calculate_perimeter(self):
#         area = self.a * 4
#         return area
#
#     def change_size(self, value):
#         self.a += value
#
#     def __repr__(self):
#         return '{0} на {0} на {0} на {0}'.format(self.a)
#
#
# s = Square(10)
# a = s
# b = Square(3)
# print(s)
#
#
# def check(obj1, obj2):
#     if obj1 is obj2:
#         return True
#     else:
#         return False
#
#
# print(check(s, a))
# print(check(s, b))
#
# class Horse:
#     def __init__(self, color, owner):
#         self.color = color
#         self.owner = owner
#
#
# class Rider:
#     def __init__(self, name):
#         self.name = name

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amount = amount
#
#     @classmethod
#     def from_string(cls, emp_str):
#         first, last, pay = emp_str.split('-')
#         return cls(first, last, pay)
#
#     @staticmethod
#     def is_workday(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return False
#         return True
#
#     def __repr__(self):
#         return f"Employee('{self.first}', '{self.last}', {self.pay})"
#
#     def __str__(self):
#         return f'{self.fullname()} - {self.email}'
#
#     def __add__(self, other):
#         return self.pay + other.pay
# # class Developer(Employee):
# #     raise_amount = 1.10
# #
# #     def __init__(self, first, last, pay, prog_lang):
# #         super(Developer, self).__init__(first, last, pay)
# #         self.prog_lang = prog_lang
# #
# #
# # class Manager(Employee):
# #
# #     def __init__(self, first, last, pay, employees=None):
# #         super(Manager, self).__init__(first, last, pay)
# #         if employees is None:
# #             self.employees = []
# #         else:
# #             self.employees = employees
# #
# #     def add_emp(self, emp):
# #         if emp not in self.employees:
# #             self.employees.append(emp)
# #
# #     def remove_emp(self, emp):
# #         if emp in self.employees:
# #             self.employees.remove(emp)
# #
# #     def print_emps(self):
# #         for emp in self.employees:
# #             print('-->', emp.fullname())
# #
# #
#
#     def __len__(self):
#         return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
# print(len(emp_1))
# print(emp_1 + emp_2)

# print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))
#
# print(emp_1.__repr__())
# print(emp_1.__str__())

# mgr_1 = Manager('Sue', "Smith", 90000, [dev_1])
#
# print(mgr_1.email)
#
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
#
# mgr_1.print_emps()




# import datetime
# my_date = datetime.date(2023, 7, 25)
#
# print(Employee.is_workday(my_date))

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'
#
# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.__dict__)
# print(emp_2.pay)
# emp_2.apply_raise()
# print(emp_2.pay)


