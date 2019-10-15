
# # # num = 100


# # # def add(a, b):
# # #     num = a + b
# # #     print(num)


# # # print(num)

# # # add(1, 2)


# # def demo():
# #     c = 10
# #     for i in range(0, 10):
# #         a = 'tiger'
# #         c += 1
# #     print(a)
# #     print(c)


# # demo()


# c = 1


# def func1():
#     c = 2

#     def func2():
#         c = 3
#         print(c)
#     func2()


# func1()


def demo():
    global c
    c = 100


demo()
print(c)
