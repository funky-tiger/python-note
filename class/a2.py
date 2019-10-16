class Student():
    name = 'initial'
    age = 10

    def __init__(self, name, age):
        self.name = name  # 通过构造函数初始化对象的属性
        age = age

    def get_info(self):  # 方法的第一个参数 必须加关键字self 类似JS中this
        print('name: '+self.name)
        print('age: '+str(self.age))


student1 = Student('tiger', 25)

print(student1.name)
print(Student.__dict__)
print(student1.__dict__)
