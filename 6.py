# -*- coding: utf-8 -*-
# @Time    : 2020/8/15 0015 21:46
# @Author  : zhengwei
# @File    : 6.py
# @Software: PyCharm
class Solution:
    def convert(self, s, numRows):
        l = len(s)
        cur_l = 2*numRows -2
        if cur_l <= 0:
            return s
        tmp = [[] for i in range(numRows)]
        for i in range(l):
            div = i // cur_l
            mod = i % cur_l
            if mod >= numRows:
                mod = cur_l - mod
            tmp[mod].append(s[i])
        result = []
        for j in range(len(tmp)):
            result.extend(tmp[j])
        return ''.join(result)
test = Solution()
result = test.convert('A', 1)
print(result)




