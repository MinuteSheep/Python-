#!/Users/minutesheep/.pyenv/shims/python
# -*- coding: utf-8 -*-


def isPower(n):
    '''
    判断是否为2的n次方
    '''
    try:
        if n&(n-1) == 0:
            return print('是2的n次方')
        return print('不是2的n次方')
    except:
        return print('错误：只接收数字')


if __name__ == '__main__':
    test_num = 2048
    isPower(test_num)
