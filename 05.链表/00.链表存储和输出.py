#!/usr/bin/env python
# coding=utf-8
# author: zhuyuan

# ## 问题: 给一个数n，并给n个元素的值，要求存成链表形式，并遍历链表输出。


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


if __name__ == '__main__':
    # 输入n, 初始化链表
    n = int(raw_input())
    root = ListNode(0)
    cur_node = root

    # 输入n个数字, 并建立链表
    for i in xrange(n):
        value = int(raw_input())
        cur_node.next = ListNode(value)
        cur_node = cur_node.next

    # 输出该链表
    cur_node = root.next
    while cur_node:
        print cur_node.val
        cur_node = cur_node.next






