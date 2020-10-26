# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 0017 19:17
# @Author  : zhengwei
# @File    : 8.py
# @Software: PyCharm
class Solution:
    def myAtoi(self, st: str) -> int:
        result = []
        is_first = False
        s = list(st)
        for i in range(len(s)):
            if s[i] == ' ':
                if is_first:
                    break
                else:
                    continue
            elif s[i].isdigit():
                result.append(s[i])
                is_first = True
            elif s[i] == '+' or s[i] == '-':
                if is_first:
                    break
                else:
                    result.append(s[i])
                    is_first = True
            else:
                break
        if len(result) <= 0:
            return 0
        elif len(result) == 1:
            if result[0].isdigit():
                return int(result[0])
            else:
                return 0
        else:
            tmp = ''.join(result)
            tmp = int(tmp)
            tmp = min(max(-1*pow(2,31), tmp), pow(2,31)-1)
            return tmp

test = Solution()
result = test.myAtoi('words and 987')
print(result)







