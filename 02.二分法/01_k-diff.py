#!/usr/bin/env python
# coding=utf-8
# author: zhuyuan

# ### 问题：给你一个list，求这个list中的k-diff对，k-diff对的定义
#          1.两元素的绝对值为k
#          2.(a, b) 和(b, a)为 同一个k-diff对


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        if k < 0:
            return 0
        if k == 0:
            counter = Counter(nums)
            return len([num for num, count in counter.iteritems() if count != 1])
        else:
            k_diff = 0
            sort_list = sorted(list(set(nums)))
            # print "sort_list:", sort_list
            for num in sort_list:
                if self.er_fen_find(sort_list, num + k):
                    k_diff += 1
            return k_diff

    def er_fen_find(self, sort_list, k):
        l, r = 0, len(sort_list) - 1
        while l <= r:
            mid = (r + l) / 2
            if sort_list[mid] == k:
                return True
            elif sort_list[mid] < k:
                l = mid + 1
            else:
                r = mid - 1
        return False


if __name__ == '__main__':
    nums = [3, 1, 4, 1, 5, 2, 3]
    k = 0
    obj = Solution()
    print obj.findPairs(nums, k)
