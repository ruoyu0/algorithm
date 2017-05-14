#!/usr/bin/env python
# coding=utf-8
# author: zhuyuan

# 问题：给你一个list，请用快速排序实现排序


class Solution(object):
    def qsort(self, seq):
        if len(seq) <= 1:
            return seq
        else:
            pivot = seq[0]
            lesser = self.qsort([x for x in seq[1:] if x < pivot])
            greater = self.qsort([x for x in seq[1:] if x >= pivot])
            return lesser + [pivot] + greater


if __name__ == '__main__':
    arr = [0, -3, 2, 5, -2, 6, 1000020, -232323]
    obj = Solution()
    qsort_res = obj.qsort(arr)
    print qsort_res
