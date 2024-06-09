Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> test_list = ['one', 'two', 'three']
>>> for i in test_list:
...     x = i + '!'
...     print(x)
... 
...     
one!
two!
three!
>>> 
>>> number = 0
>>> for score in [90, 25, 67, 45, 93]:
...     number += 1
...     if score >= 60:
...         print("%d번 학생은 합격입니다." %number)
...     else:
...         print("%d번 학생은 불합격입니다." %number)
... 
...         
1번 학생은 합격입니다.
2번 학생은 불합격입니다.
3번 학생은 합격입니다.
4번 학생은 불합격입니다.
5번 학생은 합격입니다.
