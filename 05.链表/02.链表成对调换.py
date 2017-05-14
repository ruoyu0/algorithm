#!/usr/bin/env python
# coding=utf-8
# author: zhuyuan

# ## 问题：输入n和n个数，组成链表，并对其进行成对调换，并输出


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swap_pairs(self, head):
        if head != None and head.next != None:
            next = head.next
            head.next = self.swapPairs(next.next)
            next.next = head
            return next
        return head


if __name__ == '__main__':
    # 输入
    n = int(raw_input())
    print n
    li = [int(i) for i in raw_input().split()]
    print li

    # 链表构造
    head = ListNode("head")
    cur_node = head
    for i in li:
        cur_node.next = ListNode(i)
        cur_node = cur_node.next

    # 打印链表
    cur_node = head.next
    while cur_node:
        print cur_node.val,
        cur_node = cur_node.next
    print ""

    # 链表成对调换
    cur_node = head
    while cur_node.next and cur_node.next.next:
        # 1.添加第一节点指针，第二节点指针，第三节点指针
        next1_node = cur_node.next
        next2_node = cur_node.next.next
        next3_node = cur_node.next.next.next
        # 2.cur_node连第二节点
        cur_node.next = next2_node
        # 3.第二节点连第一节点
        next2_node.next = next1_node
        # 4.第一节点连第三节点
        next1_node.next = next3_node
        # 5.head向后移两位
        cur_node = cur_node.next.next

    # 打印链表
    cur_node = head.next
    while cur_node:
        print cur_node.val,
        cur_node = cur_node.next
    print ""
