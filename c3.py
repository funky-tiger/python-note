# coding=utf-8

'''
文档说明
'''
ACCOUNT = 'admin'
PASSWORD = '123'

print('请输入账号')
user_account = input()
print('请输入密码')
user_password = input()

if user_account == ACCOUNT and user_password == PASSWORD:
    print('登录 success!')
else:
    print('token过期 fail!')
