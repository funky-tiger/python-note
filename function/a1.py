

# # # def add(a, b):
# # #     return a+b

# # # print(add(1, 2))

# # # def printValue():
# # #     print('请输入:')
# # #     v = input()
# # #     print(v)

# # # printValue()


# # # def getValue(a, b):
# # #     val1 = a*2
# # #     val2 = b + 26
# # #     return val1, val2


# # # valA, valB = getValue(1, 2)
# # # print(valA, valB)


# # def add(a, b):
# #     return a+b


# # c = add(b=3, a=2)

# # print(c)


# def getInfo(name, age=25, sex='男', blood='O'):
#     print('姓名:'+name)
#     print('年龄:'+str(age))
#     print('性别:'+sex)
#     print('血型:'+blood)


# getInfo('tiger', blood='100')


# def demo(*param):
#     print(param1)
#     print(param2)
#     print(param)
# print(type(param))
# python自动将可变参数列表对应的实参组装成一个元祖tuple


# demo(1)
# demo(1, 2, 3)
# demo('tiger', 'tiger', 'tiger')
# demo(*(1, 2, 3))

# demo('tiger', 200, 1, 2, 3, 4, 5, 6, 7, 8, 9)


# def squsum(*param):
#     sum = 0
#     for i in param:
#         sum += i * i
#     print(sum)


# squsum(1, 2)


def city_temp(**param):
    print(param)
    for key, value in param.items():
        print(key+' : '+value)


d = {'bj': '35c', 'sh': '37c', 'gd': '38c', 'sz': '38c', 'hz': '36c'}

city_temp(**d)
