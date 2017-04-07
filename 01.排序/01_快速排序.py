#!/usr/bin/env python
# coding=utf-8
# author: zhuyuan

# 问题：给你一个list，请用快速排序实现排序


class Solution(object):
    def t_sort(self, arr, start, end):
        if start >= end:
            return
        l, r, temp = start, end, arr[start]
        while l < r:
            while r > l and arr[r] > temp:
                r -= 1
            if l < r:
                arr[l] = arr[r]
                l += 1
            while l < r and arr[l] < temp:
                l += 1
            if l < r:
                arr[r] = arr[l]
                r -= 1
        arr[l] = temp
        self.t_sort(arr, start, l - 1)
        self.t_sort(arr, l + 1, end)


arr = [0, -3, 2, 5, -2, 6, 1000020, -232323]

obj = Solution()
obj.t_sort(arr, 0, len(arr) - 1)

print arr
