#!/usr/bin/env python
# coding=utf-8
# author: zhuyuan


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def rev_linklist(head):
    if head == None: #为None，直接返回 如果链表
        return None, None
    if head.next == None: # 如果链表为最后一个节点，特殊处理
        return head, head
    new_head, tail = rev_linklist(head.next)
    tail.next = head
    head.next = None
    return new_head, head # 返回链表头和链表尾


def print_linklist(linklist):
    cur_node = linklist
    while cur_node:
        print cur_node.data,
        cur_node = cur_node.next
    print ""


if __name__ == '__main__':
    link = Node(1, Node(2, Node(3)))
    # 输出
    print_linklist(link)
    # 逆置
    new_link, tail_node = rev_linklist(link)
    # 输出
    print_linklist(new_link)
