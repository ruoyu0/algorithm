#!/usr/bin/env python
# coding=utf-8
# author: zhuyuan


def print_everythind(*args):
    for count, thing in enumerate(args):
        print '{0}. {1}'.format(count, thing)


print_everythind('apple', 'banana', 'cabbage')


def table_things(**kwargs):
    for name, value in kwargs.items():
        print '{0} = {1}'.format(name, value)
table_things(apple='fruit', cabbage='vegtable')