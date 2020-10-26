# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 0016 19:23
# @Author  : zhengwei
# @File    : 7.py
# @Software: PyCharm


class Solution:
    def reverse(self, x):
        flag = 1
        if x < 0:
            flag = -1
        x = abs(x)
        result = []
        while True:
            div = x // 10
            mod = x % 10
            if div == 0:
                result.append(mod)
                break
            else:
                result.append(mod)
                x = div
        s = 0
        for i in range(len(result)):
            s = s + result[i] * pow(10, len(result) - 1 - i)
        s = s * flag
        if s >= -1 * pow(2, 31) and s <= pow(2, 31) - 1:
            return s
        else:
            return 0



test = Solution()
result = test.reverse(0)
print(result)
