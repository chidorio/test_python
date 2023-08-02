import datetime


person = {'name': 'Jehn', 'age': 23}

# sentence = 'My name is {0} and I am {1} years old'.format(person['name'], person['age'])
# print(sentence)

# tag = 'h1'
# text = 'This ia a headline'
#
# sentence = '<{0}>{1}</{0}>'.format(tag, text)
# print(sentence)

# sentence = 'My name is {0[name]} and I am {1[age]} years old'.format(person)
# print(sentence)
#
# l = ['Jehn', 23]
# sentence = 'My name is {0} and I am {1} years old'.format(l[0], l[1])
# print(sentence)

# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# p1 = Person('Jack', 23)
# sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
# print(sentence)
#
# sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age=23)
# print(sentence)
#
# person = {'name': 'Jehn', 'age': 23}
# sentence = 'My name is {name} and I am {age} years old.'.format(**person)
# print(sentence)
#
# for i in range(1, 11):
#     sentence = 'The value is {:02}'.format(i)
#     print(sentence)

# from math import pi
#
# sentence = 'sdfsdfsdfdsf {:.2f}'.format(pi)
# print(sentence)

# sentence = 'sdlfsdf to {:,.2f}'.format(1000**2)
# print(sentence)


my_date = datetime.datetime(2016, 9, 24, 13, 30, 45)

# sentence = '{:%B %d, %Y}'.format(my_date)
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)