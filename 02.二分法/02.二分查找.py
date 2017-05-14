#!/usr/bin/env python
# coding=utf-8
# author: zhuyuan


def binary_search(li, t):
    low, high = 0, len(li) - 1
    while low < high:
        print low, high
        mid = (low + high) / 2
        if li[mid] > t:
            high = mid
        elif li[mid] < t:
            low = mid + 1
        else:
            return mid
    return low if li[low] == t else False

if __name__ == '__main__':
    l = [1, 4, 12, 45, 66, 99, 120, 444]
    print binary_search(l, 12)
    print binary_search(l, 1)
    print binary_search(l, 13)
    print binary_search(l, 444)
