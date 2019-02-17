#!/Users/minutesheep/.pyenv/shims/python
# -*- coding: utf-8 -*-


def isDup(strs):
    '''
    判断字符串是否有重复字符
    '''
    for ch in strs:
        counts = strs.count(ch)
        if counts > 1:
            return True
    return False


if __name__ == '__main__':
    strs = 'Good'
    result = isDup(strs)
    print(strs + '有重复字符') if result else print(strs + '没有重复字符')
