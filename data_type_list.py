Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = [1, 2, 3]
b = ['Life', 'is', 'too', 'short']
c = [1, 2, 'Life', 'is']
d = [1, 2, [3, 4], ['Life', 'is']]

d[0]
1
d[2]
[3, 4]
d[3]
['Life', 'is']
d[3][-1]
'is'

d[0:3]
[1, 2, [3, 4]]

# 리스트 연결
a + b
[1, 2, 3, 'Life', 'is', 'too', 'short']
b[0] + " hi~ ^^;"
'Life hi~ ^^;'
a[0] + " hi~ ^^;"
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a[0] + " hi~ ^^;"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
# a[0]은 int형이기 때문에 에러 발생

# 리스트 반복
a * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]

# 리스트 수정
a[2] = 99
a
[1, 2, 99]
a[1:2] = ['a', 'b', 'c']
a
[1, 'a', 'b', 'c', 99]
a[-1] = ['d', 'e', 'f']
a
[1, 'a', 'b', 'c', ['d', 'e', 'f']]

# 삭제
del a[-1]
a
[1, 'a', 'b', 'c']

# 추가
a.append(5)
a
[1, 'a', 'b', 'c', 5]
>>> 
>>> # 정렬
>>> b.sort()
>>> b
['Life', 'is', 'short', 'too']
>>> 
>>> a = [3, 4, 1, 9]
>>> a.reverse()
>>> a
[9, 1, 4, 3]
>>> 
>>> # 위치 확인
>>> a.index(9)
0
>>> 
>>> # 원소 삽입
>>> a.insert(0, 99)
>>> a
[99, 9, 1, 4, 3]
>>> 
>>> # 원소 삭제
>>> a.remove(99)
>>> a
[9, 1, 4, 3]
>>> b = [1, 2, 3]
>>> b.pop()
3
>>> b
[1, 2]
>>> b.pop(0)
1
>>> b
[2]
>>> 
>>> # 특정 원소값 개수
>>> a = [2, 1, 0, 2, 3, 2, 4, 2]
>>> a.count(2)
4
