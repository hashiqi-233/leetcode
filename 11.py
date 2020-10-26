# -*- coding: utf-8 -*-
# @Time    : 2020/8/30 0030 16:24
# @Author  : zhengwei
# @File    : 11.py
# @Software: PyCharm
class Solution:
    def maxArea(self, height):
        max_area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            area = (j - i) * min(height[i], height[j])
            if area >= max_area:
                max_area = area
            if height[i] >= height[j]:
                j = j-1
            else:
                i = i+1
        return max_area

test = Solution()
result = test.maxArea([1,8,6,2,5,4,8,3,7])
print(result)







