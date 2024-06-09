Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# 비교 연산자
>>> x = 3
>>> y = 2
>>> 
>>> x == y
False
>>> x != y
True
>>> x >= y
True
>>> 
>>> # 조건 연결
>>> money = 1300
>>> if money >= 1200 and money < 3500:
...     print("버스를 탈 수 있습니다.")
... 
...     
버스를 탈 수 있습니다.
>>> # and, or, not 이 있음
>>> 
>>> # 그룹 자료형 원소 검사
>>> 1 in [1, 2, 3]
True
>>> x in [1, 2, 3]
True
>>> x not in [1, 2, 3]
False
>>> 'a' in ('a', 'b', 'c', 'd')
True
>>> 'i' not in 'Python'
True
>>> 
>>> # 아무 것도 하지 않게 설정하기
>>> if money < 10:
...     pass
... else:
...     print("저금하자!")
... 
...     
저금하자!
