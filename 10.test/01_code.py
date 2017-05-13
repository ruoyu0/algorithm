#!/usr/bin/env python
# coding=utf-8
# author: zhuyuan

a, b = 0, 1

while b < 100:
    print (b),
    a, b = b, a + b
