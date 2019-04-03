#!/usr/bin/env python3
import sys
s = 'python'

print(s)  # 输出字符串
print(s[0:-1])  # 输出第一个到倒数第二个的所有字符
print(s[0])  # 输出字符串第一个字符
print(s[2:5])  # 输出从第三个开始到第五个的字符
print(s[2:])  # 输出从第三个开始的后的所有字符
print(s * 2)  # 输出字符串两次
print(s
      + '你好')  # 连接字符串

print('------------------------------')

print('hello \n runoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\n runoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
abc = input("\n\n按下 enter 键后退出。")

print(abc)
print(sys.api_version)
print(sys.copyright)




