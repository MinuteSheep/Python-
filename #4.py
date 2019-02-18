#!/Users/minutesheep/.pyenv/shims/python
# -*- coding: utf-8 -*-


def isInt(string):
    '''
    判断传入的字符串是否为整数
    '''
    try:
        num = int(string)
        print(num)
    except Exception:
        print('不是整数')


str1 = '123'
str2 = '-123'
str3 = '0'
str4 = '1.2'
str5 = 'sfs'

isInt(str1)
isInt(str2)
isInt(str3)
isInt(str4)
isInt(str5)
