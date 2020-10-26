# -*- coding: utf-8 -*-
# @Time    : 2020/10/8 0008 15:58
# @Author  : zhengwei
# @File    : 26.py
# @Software: PyCharm

class Solution:
    def removeDuplicates(self, nums):
        i = 0
        j = 1
        while j <= len(nums)-1:
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i = i+1
                j = j+1
            else:
                j = j+1
        return len(nums[:i+1])

test = Solution()
result = test.removeDuplicates([1,1, 2,2222])
print(result)





