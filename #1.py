#!/Users/minutesheep/.pyenv/shims/python
# -*- coding: utf-8 -*-

ans = [i*100+j*10+k for i in range(1, 5) for j in range(1, 5)
       for k in range(1, 5) if i != j and i != k and j != k]
print(ans)
