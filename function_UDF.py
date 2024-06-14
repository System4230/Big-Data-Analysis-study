Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 함수 정의
>>> def sum1(a, b):
...     x = a + b
...     return x
... 
>>> def sum2(*args):
...     x = 0
...     for i in args:
...         x += i
...     return x
... 
>>> 
>>> # 함수 호출
>>> a = 5
>>> b = 3
>>> sum1(a, b)
8
>>> sum1(3, 5)
8
>>> sum2(1, 2, 3, 4, 5)
15
>>> sum2(2, 3.5, 10)
15.5
