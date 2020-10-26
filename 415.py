# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 0003 20:56
# @Author  : zhengwei
# @File    : 415.py
# @Software: PyCharm


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        s1 = num1[::-1]
        s2 = num2[::-1]
        # if len(s1) < len(s2):
        #     s1, s2 = s2, s1
        l1 = len(s1)
        l2 = len(s2)
        add_flag = 0
        result = []
        if l1 < l2:
            s1 = num2[::-1]
            s2 = num1[::-1]
            l1 = len(s1)
            l2 = len(s2)
        for i in range(l1):
            if 0 <= i <= l2-1:
                tmp = int(s1[i]) + int(s2[i]) + add_flag
                if tmp > 9:
                    add_flag = 1
                    tmp = tmp - 10
                else:
                    add_flag = 0
                result.append(str(tmp))
            else:
                if add_flag == 0:
                    result.append(s1[i])
                else:
                    tmp = int(s1[i]) + add_flag
                    if tmp > 9:
                        add_flag = 1
                        tmp = tmp - 10
                    else:
                        add_flag = 0
                    result.append(str(tmp))
        if add_flag == 1:
            result.append(str(add_flag))
        result.reverse()
        return ''.join(result)

test = Solution()
result = test.addStrings(num1='9', num2='99')
print(result)














