Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t1 = (1, )
>>> t2 = (1, 2, 3)
>>> t3 = 1, 2, 3
>>> t4 = (1, 2, (3, 4), ('Life', 'is'))
>>> 
>>> t4 [0]
1
>>> t4 [3][-1]
'is'
>>> 
>>> t4[0:3]
(1, 2, (3, 4))
>>> 
>>> t1 + t2
(1, 1, 2, 3)
>>> 
>>> t1 + "hi~ ^^;"
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    t1 + "hi~ ^^;"
TypeError: can only concatenate tuple (not "str") to tuple
>>> # 튜플과 문자열은 연결 불가
>>> 
>>> t2 * 3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> 
>>> t2[2] = 99
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    t2[2] = 99
TypeError: 'tuple' object does not support item assignment
>>> # 튜플은 수정이 불가
