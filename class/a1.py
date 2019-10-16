class Student():
    sums = 100
    name = ''
    age = 10

    # 构造函数 该函数在实例化的时候是自动调用的
    def __init__(self, name, age):
        # 对于构造函数 不能手动返回除了NoneType之外的类型 只能返回NoneType
        # return '调用了构造函数'
        self.name = name  # 通过构造函数初始化对象的属性
        self.age = age
        # print(name)
        # print(age)

    def get_info(self):  # 方法的第一个参数 必须加关键字self 类似JS中this
        print('类变量: '+str(Student.sums))


# 实例化 不用通过new关键字来实例化
student1 = Student('tiger', 25)
# student2 = Student('pig', 26)
# student3 = Student('cat', 28)
student1.get_info()
