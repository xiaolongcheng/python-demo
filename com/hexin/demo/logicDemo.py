#!/usr/bin/python3

a = 21
b = 10
c = 0

if (a == b) and (False < True):
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")

if a != b:
    print("2 - a 不等于 b")
else:
    print("2 - a 等于 b")

if a < b:
    print("3 - a 小于 b")
else:
    print("3 - a 大于等于 b")

if a > b:
    print("4 - a 大于 b")
else:
    print("4 - a 小于等于 b")

# 修改变量 a 和 b 的值
a = 5
b = 20
if a <= b:
    print("5 - a 小于等于 b")
else:
    print("5 - a 大于  b")

if b >= a:
    print("6 - b 大于等于 a")
else:
    print("6 - b 小于 a")

a = 10
b = 20
list1 = [1, 2, 3, 4, 5]

if a in list1:
    print("1 - 变量 a 在给定的列表中 list 中")
else:
    print("1 - 变量 a 不在给定的列表中 list 中")

if b not in list1:
    print("2 - 变量 b 不在给定的列表中 list 中")
else:
    print("2 - 变量 b 在给定的列表中 list 中")

