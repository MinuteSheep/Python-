#!/Users/minutesheep/.pyenv/shims/python
# -*- coding: utf-8 -*-


def func(num):
    '''
    递归调用自己，每次打印参数
    '''
    print(num)
    if num > 1:
        func(num-1)


if __name__ == '__main__':
    func(100)
