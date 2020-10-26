# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 0006 10:01
# @Author  : zhengwei
# @File    : 13.py
# @Software: PyCharm


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        int_num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        d_room_int = dict(zip(roman, int_num))
        result = 0
        i = 0
        while i <= len(s) - 1:
            if s[i:i+2] in d_room_int:
                result = result + d_room_int[s[i:i+2]]
                i = i + 2
            elif s[i] in d_room_int:
                result = result + d_room_int[s[i]]
                i = i+1
            else:
                pass
        return result

test = Solution()
result = test.romanToInt('MCMXCIV')
print(result)





