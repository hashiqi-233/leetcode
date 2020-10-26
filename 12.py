# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 0031 20:39
# @Author  : zhengwei
# @File    : 12.py
# @Software: PyCharm

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        int_num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        results = []
        while num > 0:
            for idx in range(len(int_num)):
                if num - int_num[idx] >= 0:
                    results.append(roman[idx])
                    num = num - int_num[idx]
                    break
        return ''.join(results)

test = Solution()
result = test.intToRoman(2000)
print(result)







