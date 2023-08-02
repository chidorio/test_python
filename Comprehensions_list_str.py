# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_list = []
# for i in nums:
#     my_list.append(i)
# my_list_smart = [n for n in nums]
# my_list_smart2 = [n * n for n in nums]
# my_list_smart3 = map(lambda n: n * n, nums)
# my_list_smart4 = filter(lambda n: n % 2 == 0, nums)
#
#
#
#
# print(my_list_smart)
# print(my_list_smart2)
# print(my_list_smart3)

# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))
# print(my_list)
# my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
# print(my_list)

names = ['Bruce', 'Clark', 'Peter']
heroes = ['Batman', 'Superman', 'Spiderman']
# dict = zip(names, heroes)
# for key, value in dict:
#     print(key, value)

# my_dict = {}
# for name, hero in zip(names, heroes):
#     my_dict[name] = hero

# my_dict = {name : hero for name, hero in zip(names,heroes) if name != 'Peter'}
# print(my_dict)


# GENERATOR EXPRESSIONS
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def gen_func(nums):
    for n in nums:
        yield n * n


my_gen = gen_func(nums)

for i in my_gen:
    print(i)