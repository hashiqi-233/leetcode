# -*- coding: utf-8 -*-
# @Time    : 2020/10/9 0009 21:39
# @Author  : zhengwei
# @File    : 27.py
# @Software: PyCharm

class Solution:
    def removeElement(self, nums, val):
        i = 0
        j = 0
        while j <= len(nums)-1:
            if nums[j] == val:
                j = j+1
            else:
                nums[i] = nums[j]
                i = i + 1
                j = j+1
        return len(nums[:i])
test = Solution()
result = test.removeElement([2,3,3,2,5,7],5)
print(result)


