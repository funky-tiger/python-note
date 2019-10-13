## Python

- 编译型语言 C C++
  > 直接编译成机器码 而机器码十分接近底层
- 解释型语言 JS Python
  > 需要解释器去解释代码 解释的过程比较慢

## 基本数据类型

### Number 数字

> 整型(int) 浮点型 (float) 布尔类型(bool) 复数(complex)

- 整型(int)

  - 其他语言的整数
    > (short) (int) (long)
  - 其他语言的浮点数
    > 单精度(float) 双精度(double)

  ```python
  >>> type(1)
  <class 'int'>
  >>> type(1.0)
  <class 'float'>
  >>> type(1+1.0)
  <class 'float'>
  >>> type(-1)
  <class 'int'>
  >>> type(-1.0)
  <class 'float'>
  >>> type(1/2)
  <class 'float'>  单 / 得到float类型的number
  >>> type(1//2)
  <class 'int'>  双 // 得到int类型的number
  >>> 1//2
  0  双 //  是 整除 只保留整数部分
  ```

  - 进制

    - 2 进制 0b10 -> 表示二进制的 10
    - 8 进制 0o10 -> 表示八进制的 10
    - 16 进制 0x10 -> 表示十六进制的 10

    - 进制转换
      - bin 方法 转换为二进制
      ```python
      >>> bin(10) // 转换十进制
      '0b1010'
      >>> bin(0x18) // 转换十六进制
      '0b11000'
      >>> bin(0xE) // 转换十六进制
      '0b1110'
      ```
      - int 方法 转换为十进制
      ```python
      >>> int(0x19) // 转换十六进制
        25
        >>> int(0b111) // 转换二进制
        7
        >>> int(0o111) // 转换八进制
        73
        >>> int(0x111) // 转换十六进制
        273
      ```
      - hex 方法 转换为十六进制
      ```python
        >>> hex(10) // 转换十进制
        '0xa'
        >>> hex(888) // 转换十进制
        '0x378'
        >>> hex(0o777) // 转换八进制
        '0x1ff'
      ```
      - oct 方法 转换为八进制
      ```python
      >>> oct(8)
        '0o10'
        >>> oct(0b111)
        '0o7'
        >>> oct(0x10)
        '0o20'
      ```

- 布尔类型(bool)

  ```python
    >>> type(False)
    <class 'bool'>  // bool类型
    >>> type(True)
    <class 'bool'> // bool类型
    >>> int(True)
    1              // 因为布尔类型是数字的子类型， 所以True可以转换为1
    >>> int(False)
    0
    >>> bool(0.5) // 非0 非空的数值 都是bool真值
    True
    >>> bool(-1)
    True
    >>> bool(0) // 数值0 都是bool假值
    False
    >>> bool('') // 空str 都是bool假值
    False
    >>> bool([]) // 空列表 都是bool假值
    False
    >>> bool({}) // 空元祖 都是bool假值
    False
    >>> bool(None) // 类型NoneType 都是bool假值
    False
  ```

- 复数(complex)
  > 使用小写字母 j 来表示复数
  ```python
  >>> 35j
    35j
  ```

### 字符串 str

- 单双引号配合
  ```python
    >>> "let's go baby!" // 单双引号区分
    "let's go baby!"
    >>> 'let"s go baby~'
    'let"s go baby~'
    >>> 'let\'s go baby.' // 转义字符
    "let's go baby."
  ```
- 三引号多行换行

  ```python
    >>> '''
    python字符串换行 有点像markdown
    python字符串换行 有点像markdown
    python字符串换行 有点像markdown
    '''
    '\npython字符串换行 有点像markdown\npython字符串换行 有点像markdown\npython字符串换行 有点像markdown\n'

    >>> print('反斜杠n的作用\n是回车\n测试')
    反斜杠n的作用
    是回车
    测试
    >>>
  ```

  - 转义字符

    - 特殊的字符
      > 无法 看见 的字符 `/n`
      > 与语言本身语法有冲突的字符 `' "`
      > \n 换行 \' 单引号 \t 横向制表符

    ```python
    >>> print('hello \\n world')  通过双反斜杠\\ 来转义\n
      hello \n world

    >>> print(r'hello \n world')  通过前面加小写r 来来转义\n 加r之后变成原始字符串
      hello \n world
    ```

  - 字符串运算

  ```python
  >>> 'hello'+'world' // 简单字符串拼接
  'helloworld'
  >>> 'hello'*3  // 字符串想乘
  'hellohellohello'
  >>> 'helloworld'[0]  // 通过下标获取字符串单个元素
  'h'
  >>> 'helloworld'[-1]  // 从字符串的末尾开始数
  'd'
  >>> 'helloworld'[-3]
  'r'
  ```

  - 字符串截取
    ```python
    >>> 'helloworld'[0:5]  // 截取 从下标0开始向前数5位
      'hello'
    >>> 'helloworld'[0:-1]  // 截取 从下标0开始向后数1位
      'helloworl'
    >>> 'helloworld'[5:]  //  从向前数5个下标 自动截取到字符串的末尾
      'world'
    >>> 'helloworld'[-5:]  // 从向后数5个下标 自动截取到字符串的末尾
      'world'
    >>> 'helloworld'[:-5] // 从下标0开始 向后数5位
      'hello'
    >>> 'helloworld'[:5] // 从下标0开始 向前数5位
      'hello'
    ```

### 列表 list

- 动态数组
  ```python
  >>> [1,2,3,4,5,6] // 逗号分隔开
  [1, 2, 3, 4, 5, 6]
  >>> type([1,2,3,4,5,6])  // list类型
  <class 'list'>
  >>> [1,'str',2,True,3,4,False,5,6]  // 列表元素可以有多种类型
  [1, 'str', 2, True, 3, 4, False, 5, 6]
  >>>
  ```
- 列表的基本操作
  - 访问 截取
    ```python
    >>> ['新月打击', '苍白之瀑', '月之降临', '月神冲刺'][1] // 访问列表中的某个元素
    '苍白之瀑'
    >>> ['新月打击', '苍白之瀑', '月之降临', '月神冲刺'][0:2] // 截取列表
    ['新月打击', '苍白之瀑']
    >>> ['新月打击', '苍白之瀑', '月之降临', '月神冲刺'][0:1] // 截取列表
    ['新月打击']
    >>> ['新月打击', '苍白之瀑', '月之降临', '月神冲刺'][-1:] // 反向截取列表
    ['月神冲刺']
    ```
  - 列表的运算
    ```python
    >>> ['新月打击','苍白之瀑','月之降临','月神冲刺']+['闪现','引燃'] //类似于.concat()
    ['新月打击', '苍白之瀑', '月之降临', '月神冲刺', '闪现', '引燃']
    >>> ['新月打击'] * 2  // 列表的乘法
    ['新月打击', '新月打击']
    ```
  - 判断元素是否存在
  ```python
  >>> 3 in [1,2,3]
  True
  >>> 3 in [7,8,9]
  False
  >>> 3 not in [7,8,9]
  True
  ```

### 元组 tuple

- 元组的定义和列表基本一致

  ```python
  >>> type((1,2,3)) // tuple元祖类型
  <class 'tuple'>
  >>> (1,2,3,4,5,6) // 逗号隔开
  (1, 2, 3, 4, 5, 6)
  >>> (1,True,'str',2) // 元素可以有多种类型
  (1, True, 'str', 2)
  >>> (1, 2, 3, 4, 5, 6)[0] // 通过下标访问元素
  1
  >>> (1, 2, 3, 4, 5, 6)[0:3] // 元祖截取
  (1, 2, 3)
  >>> (1,2,3)+(4,5,6) // 元祖相加 类型.concat
  (1, 2, 3, 4, 5, 6)
  >>> (1,2,3)*2 // 元组乘法
  (1, 2, 3, 1, 2, 3)
  >>>
  ```

- 列表和元祖的区别

  > tuple 不可变，所以代码更安全。如果可能，能用 tuple 代替 list 就尽量用 tuple。

- 字符串 列表 元祖 它们都属于序列

  - 判断元素都是存在

  ```python
  >>> 3 in (1,2,3)
  True
  >>> 3 in (7,8,9)
  False
  >>> 3 not in (7,8,9)
  True
  ```

  - 序列长度

  ```python
  >>> len([1,2,3])
  3
  >>> len((1,2,3))
  3
  >>> len((1,))
  1
  >>> len('hello world')
  11
  ```

  - 序列的最大值/最小值

  ```python
  >>> max([1,2,3])
  3
  >>> min((1,2,3))
  1
  >>> max('helloworld')
  'w'
  >>> min('helloworld')
  'd'
  ```

  - 查看 ascll 编码

  ```python
  >>> ord('w') // ord方法接收一个参数 将其转换为ascll编码
  119
  >>> ord(' ')
  32
  >>> ord('d')
  100
  ```

### 集合 set

- 特点
  - 1. 集合无序的 序列是有序的
    ```python
    >>> {1,2,3,4,5,6}  // 大括号定义集合
    {1, 2, 3, 4, 5, 6}
    >>> type({1,2,3,4,5,6}) // 集合 set类型
    <class 'set'>
    >>> {1,2,3,4,5,6}[0] // 会报错 因为集合是无序的
    ```
  - 2. 不重复 会自动过滤掉重复的元素
    ```python
    >>> {1,1,1,2,2,2,5,6,6,7,8,7,7,7} // 自动过滤重复元素
    {1, 2, 5, 6, 7, 8}
    ```
- 集合的运算

  - 差集 交集 并集

  ```python
  >>> type(set()) // 定义一个空的集合
  <class 'set'>
  >>> len({1,2,3}) // 求集合的长度
  3
  >>> 1 in {1,2,3} // 判断某个元素是否存在于集合中
  True
  >>> 1 not in {1,2,3} // 判断某个元素是否不存在于集合中
  False
  >>> {1,2,3,4,5,6} - {3,4} // 剔除集合中的某些元素 求两个集合的差集
  {1, 2, 5, 6}
  >>> {1,2,3,4,5,6} & {3,4,7} // 求两个集合中的共有的交集
  {3, 4}
  >>> {1,2,3,4,5,6} | {3,4,7} // 求两个集合中的不重复的并集
  {1, 2, 3, 4, 5, 6, 7}
  ```

### 字典 dict

- 特点
  - key/value 形式 (类似于 js 中的对象)
  - 字典的 key 不能重复
  - 字典的 key 必须是不可变的类型 `int str tuple ...`
- 字典的相关操作
  ```python
  >>> {1:1,2:2,3:3} // key/value形式定义字典
  {1: 1, 2: 2, 3: 3}
  >>> type({1:1,2:2,3:3}) // dict类型
  <class 'dict'>
  >>> {(1,2,3):'元祖是不可变的',2:2,3:3} // 元祖是可以作为key的
  {(1, 2, 3): '元祖是不可变的', 2: 2, 3: 3}
  >>> {'Q':'新月打击', 'W':'苍白之瀑', 'E':'月之降临', 'R':'月神冲刺'}['Q'] // 通过key去访问vlue
  '新月打击'
  >>> {'Q':'新月打击', 'Q':'苍白之瀑', 'E':'月之降临', 'R':'月神冲刺'} // 字典的key不能重复
  {'Q': '苍白之瀑', 'E': '月之降临', 'R': '月神冲刺'}
  ```

## 变量

- 定义一个变量

  ```python
  >>> list = [1,2,3]
  >>> print(list)
  [1, 2, 3]
  ```

- 变量命名规范

  - 1. 变量的首位不能是数字
  - 2. 只能使用字母 数字 下划线
  - 3. 不能使用系统的保留关键字
  - 4. 变量名区分大小写
  - 5. 变量是动态类型

- 值类型和引用类型

  - 值类型 不可变 : `int(数字) str(字符串)) tuple(元祖)`
  - 引用类型 可变 : `list(列表) set(集合) dict(字典)`

  ```python
    >>> a = 1
    >>> b = a
    >>> a = 3
    >>> print(a,b) // int 是值类型
    3 1

    >>> a = [1,2,3]
    >>> b = a
    >>> a[0]='tiger'
    >>> print(a,b)  // list 是引用类型
    ['tiger', 2, 3] ['tiger', 2, 3]

    >>> b = 'hello' // 证明 str 的不可变性
    >>> id(b)       // id() 来获取变量的内存地址
    4463351920      // b 的内存地址1
    >>> b = b + 'python'
    >>> id(b)
    4463290480      // b 的内存地址2 地址已经变化 所以b的值就可以变化

    >>> 'hello'[0] = 'p' // 反向证明 直接改变 str 的某个元素 会报错 因为 str 是值类型 不可变的
    Traceback (most recent call last):
      File "<pyshell#25>", line 1, in <module>
        'hello'[0] = 'p'
    TypeError: 'str' object does not support item assignment
  ```

- 运算符

  - 算术运算符
    ```python
    >>> 1+1       // 加
    2
    >>> 'str'+'str'   // 字符串加
    'strstr'
    >>> 2-1      //减
    1
    >>> 'str'*3       //乘
    'strstrstr'
    >>> 3/2      //除
    1.5
    >>> 3//2      //整除
    1
    >>> 5%2       // 取余
    1
    >>> 2**2      // 次方 2 的 2 次方
    4
    ```
  - 赋值运算符
    ```python
    >>> c = 1
    >>> c += 1
    >>>
    c
    >>> c
    2
    >>> b = 2
    >>> a = 3
    >>> b*=a
    >>> b
    6
    >>>
    ```
  - 关系(比较)运算符
    ```python
    >>> 1==1
    True
    >>> 1>1
    False
    >>> 1>=1
    True
    >>> 1 != 1
    False
    >>> 'a'>'b'  // 字符串比较ascll码
    False
    >>> ord('a')
    97
    >>> ord('b')
    98
    >>> '123'>'789' // 多个字符串比较 会按照每一项的ascll码去比较,'1'和'7' '2'和'8' ...
    False
    >>> [1,2,3] < [7,8,9] // 所有项的ascll码都满足条件才会返回True
    True
    >>> (1,2,3) < (7,8,9) // 同上 js语言也是同样的比较规则
    True
    >>>
    ```
  - 逻辑运算符

    - and (&& 且)
    - or (|| 或)
    - not (! 去反)

    ```python
    >>> True and True // and js中的 &&
    True
    >>> True and False
    False
    >>> 1 and '1'
    '1'
    >>> True or False  // or js中的 ||
    True
    >>> True or True
    True
    >>> False or False
    False
    >>> not False   // not js中的 !
    True
    >>> not 'str'
    False
    >>> not not 'str' // not not js中的 !!
    True
    >>> not not ''
    False
    >>> not not []
    False
    ```

    - 对于 `int` 和 `float` 除了 `0` 为 `False` 之外 其他都为 `True`
    - 对于 `str` 除了空字符串为 `False` 之外 其他都为 `True`
    - 对于 `list` 除了空列表 `[]` 为 `False` 之外 其他都为 `True`
    - `tuple` `set` `dict` 遵循和 `list` 一致的规则

  - 成员运算符
    - 用来判断一个元素是否在一个组里面
    - 这个组可以是 `list` `tuple` `set` 甚至 `str`
    ```python
    >>> a = 1
    >>> a in [1,2,3]
    True
    >>> 5 in [1,2,3]
    False
    >>> a not in [1,2,3]
    False
    >>> 5 not in [1,2,3]
    True
    ```
    - 对于 dict(字典)来说 `in`或者`not in`判断的是字典的`key`而并非`value`
    ```python
    >>> str = 'a'
    >>> str in {'b':1}
    False
    >>> str = 1
    >>> str in {'b':1}
    False
    >>> str = 'b'
    >>> str in {'b':1}  // 只有`str`等于字典的`key('b')`时 才会返回`True`
    True
    ```
  - 身份运算符

    - 如果两个变量取值相等 则`is`返回`True`
    - `is` 和 `==` 的区别
      > `==` 是比较值是否相等 `is`比较的是身份（或者是内存地址）是否相等

    ```python
    >>> a = 1
    >>> b = 2
    >>> a is b
    False
    >>> a is 1
    True
    >>> a = 1
    >>> b = 1.0
    >>> a == b // == 比较的仅是值
    True
    >>> a is b
    False
    >>> id(a)  // is 比较的是内存地址
    4340726576
    >>> id(b)  // is 比较的是内存地址
    4361062352
    >>> a is not b // is not 身份不等
    True

    >>> a = {1,2,3}
    >>> b = {2,1,3}
    >>> a == b // 对于集合set来讲 == 只要是每个元素相等  不在意顺序 就会返回True
    True        // 但是 is 会返回False 因为它们的内存地址不同
    >>> id(a)    // 该特点仅对集合有效 对于list列表来讲 == 不仅要每个元素相等 还要顺序相等 才会返回Trye
    4425248112   // list 的 is也会返回Flase 因为它们的内存地址也不同
    >>> id(b)
    4453348608
    >>> a is not b
    True
    ```

    - 判断变量的值 id(身份) 和 类型
      - 在 python 中 万物皆是对象 对象的三个特征就是 值(value) 身份(id) 和类型(type)
        - 值
        ```python
        >>> a = 1
        >>> a == 1  // == 运算符 用来判断值 value
        True
        ```
        - 身份
        ```python
        >>> id(a)  // id() 方法用来查看变量的地址
        4463799088
        ```
        - 类型
        ```python
        >>> isinstance(1, int)  // isinstance()方法用来判断变量是否为第二个参数类型
        True
        >>> isinstance(1,(str,int,float)) // 第二个参数也可以是一个元祖，只要符合元祖中任意一个条件即可返回True
        True
        ```

  - 位运算符
    - 把数字当作二进制数进行运算
    - `&` 按位与
    - `|` 按位或
    - `^` 按位异或
    - `~` 按位取反
    - `<<` 左移动
    - `>>` 右移动
    ```python
    >>> a = 2  // 二进制 10
    >>> b = 3  // 二进制 11
    >>> a & b  // 每一位去比较 两位都是 `1` 才为 `1`,通过 `按位与` 计算为 `10`
    2          // 10 最终转换为 10进制 为2
    >>>
    ```

## 表达式

- 表达式是运算符和操作数所构成的序列
  ```python
  >>> 1 + 2 * 3
  7
  >>> (1 + 2) * 3 // 表达式是有序的
  9
  ```
- 表达式的优先级
  - 1. 同级情况下默认从左到右解析（术语：左结合）(有等号的情况下变成右结合)
  - 2. `*` 大于 `+`
  - 3. `and` 大于 `or`
  - 4. `not` 大于 `or`
  - 5. `not` > `and` > `or`
  ```python
  >>> 1 or 2 and 3      // and 大于 or
  1
  >>> (1 or 2) and 3     // 通过()来改变运算的优先级
  3
  >>> a = 1 + 2        // 右结合: 先计算等号右边
  >>> not 1 or 2 + 2 == 2  // (not 1) or ((2 + 2) == 2)
  False
  ```

## vscode 环境 插件配置

- 插件
  - 1. python
    - 智能感知 断点调试
  - 2. vscode-icon
    - 美化文件图标

## 流程控制语句

- 条件控制

  - `if else`

    - python 通过换行缩进来确定内部语句

    ```python
    # 1. if/else 基本用法和其他语言没有太大区别
    mood = True
    if mood:
        print('AAA')
    else:
        pass   # pass 占位符 什么都不做 类似于JS中return

    # 2. elif 分支写法
    # python中没有switch写法 可用两种方法来代替：
    # 1. 通过elif来代替
    # 2. 通过字典的key获取value来代替
    if a == 1:
        print('A')
    elif a == 2:
        print('B')
    elif a == 3:
        print('C')
    elif a == 4:
        print('D')
    else:
        print('E')
    ```

- 循环控制

  - while 循环

    - 递归场景下 比较适合使用 while

    ```python
    CONDITION = 1

    while CONDITION <= 10:  # 当 CONDITION 小于10时执行
        print(CONDITION)
        CONDITION += 1
    else:
        print('结束了')    # while可以和else进行结合 当执行完所有while后 会执行一次else
    ```

  - for 循环

    - 主要用来遍历 ` 序列``集合 `或者`字典` 但是`python`for 循环中可以使用`else`关键字
      ```python
        a = ['apple', 'banana', 'orange']
        for item in a:        # 类似于JS中的for...in...
            print(item)
        else:               # python的for循环的最后可以加一个else  它是在循环结束后执行
            print('for循环结束了')
      ```
    - break
      在 `pyhton` 的 `for` 循环中 通过 `break` 关键字来跳出循环

      ```python
      a = ['apple', 'banana', 'orange']
      for item in a:
          if item == 'orange':
              break      # break后 for循环后面所有的代码都不会执行 直接跳出for循环(else也不会执行)
          print(item)
      ```

    - continue:
      在 `pyhton` 的 `for` 循环中 通过 `continue` 关键字来跳过某次循环

      ```python
      a = ['apple', 'banana', 'orange']
      for item in a:
          if item == 'banana':
              continue     # continue后 for循环会跳过本次循环 接着执行后面的循环
          print(item)

      ```

    - range()函数 `python`中的`for(let i = 0; i < arr.length; i++){..}`

    ```python
    # c9:
    for item in range(0, 10, 2):   # range() 函数第一个参数是起始值 第二个参数是偏移量 第三个参数是步长 间隔多少 可以是负数 但不是必须参数
    print(item)
    ```

## Python 的组织管理

- 包

  - 包下面必须有一个`__init__.py`文件
  - 1. 规定包下的哪些模块可以供导出

    - 当一个包被导入的时候 不管你导入的是包还是模块变量 `__init__.py`文件都会自动执行

      ```python
      # 包名为 dir 的 __init__.py 文件:
      __all__ = ['a1']  # 可以规定该包下只有某些模块(文件)可以导出

      # 导入包的文件:
      from dir import * # 从dir包中导入所有的模块(文件)
      print(a1.a)  # 可以得到a1.a变量 因为 dir 包的 __init__.py 文件 规定了 a1文件可以导出
      print(a11.e)  # 不可以得到a11.ae变量 因为 dir 包的 __init__.py 文件 没有规定 a11 文件可以导出
      ```

  - 2. 批量导入

       - 只需在包的`__init__.py`文件中引入导入率较高的公共模块，在其他模块中只需通过引入该包 即可使用这些公共模块

       ```python
        # dir包的__init__.py:
        import sys            # 只需在包的__init__.py文件中一次导入所有模块
        import datetime       # 在其他模块中就可以通过引入该包的形式
        import io             # 来使用__init__.py中所导入的所有模块

        # 其他模块:
        import dir
        print(dir.sys.path)   # 在其他模块中不引入sys模块 也可以使用sys模块 因为dir包已经导入过了
       ```

- 模块

  > 可以理解为一个文件 但不是一个真的文件

  - 1. 通过 import 导入模块

    ```python
    # a1.py & a2.py
    import dir.a1   # 导入「命名空间」 缺点: 如果模块的层级很深时 导入模块则需要写很长的命名空间
    print(dir.a1.a)  # 变量的使用同样遵循improt导入的写法

    # 使用别名 as
    import dir.a1 as x   # 导入「命名空间」 作为 「模块别名」 此时模块x就作为dir.a1
    print(x.a)   # 使用时 可以直接使用 模块别名.变量
    ```

  - 2. 通过 from import 导入模块

    ```python
    # from import 直接导入变量
    from dir.a1 import a  # 从 「命名空间」 导入 「变量」
    print(a)  # 此处可直接使用变量 因为from import导入直接就是变量

    # from import 导入模块
    from dir import a1  # 从 「命名空间」 导入 「模块」
    print(a1.a)  #

    # from import 一次导入模块所有变量
    from dir.a1 import *  # 将模块 dir.a1 中所有变量全部导入
    print(a)
    print(b)
    print(c)
    print(d)

    # 在模块中通过模块的内置属性 __all__ ,来控制导出部分变量
    __all__ = ['a', 'b']     # 限制导出某些变量
    a = 1     # 外部模块通过 from xxx.x import *  引入该模块时
    b = 2     # 只能引入a和b两个变量
    c = 3
    d = 4
    ```

  - 3. python 中一次导入多个模块/变量

    ```python
    from dir.a1 import a, b, c,\
      d                   # 从 「命名空间」 导入 「变量, 变量, 变量...」  python中换行是行尾加 \
    from dir.a1 import (a, b, c,     # 或者用小括号对多个变量进行包裹
    d)
    print(a)
    print(b)
    print(c)
    print(d)

    ```

    - import 和 from import 的区别
      > import 导入的是一个模块 而 from import 导入的可以是一个模块也可以是一个变量

  - 4. 模块的内置变量
    ```python
     '''
         这是a22.py的注释..
     '''
     print('__name__:'+__name__)   # 模块的命名空间(模块的相对路径)
     print('__package__:'+__package__)   # 模块的包名(模块的父级目录)
     print('__doc__:'+__doc__)    # 模块的文档说明(三引号括起来的文档说明)
     print('__file__:'+__file__)    # 模块的物理路径(模块的绝对路径)
    ```

- 类

- 函数 变量

- 常见错误
  - 包和模块是不会被重复导入的
  - 避免循环导入
    > `模块1`中导入了`模块2`, `模块2`中又导入了`模块1`
