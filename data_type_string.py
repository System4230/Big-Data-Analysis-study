Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s1 = 'Hello Python'
s1
'Hello Python'
s2 = "Hello Python"
s2
'Hello Python'
s3 = '''Hello Python'''
s3
'Hello Python'
s4 = """Hello Python"""
s4
'Hello Python'

head = "Python"
tail = " is fun"
head + tail
'Python is fun'
head * 2
'PythonPython'
print("=" * 5)
=====

a = "Now is better than never"
a[0]
'N'
a[4]
'i'
a[-1]
'r'
a[-2]
'e'

b = a[0] + a[1] + a[2]
b
'Now'
a[0:3]
'Now'
a[4:6]
'is'
a[19:]
'never'
a[:3]
'Now'
a[:]
'Now is better than never'
a[7:-11]
'better'

a = "Python"
a.count('p')
0
a.find('y')
1
>>> a.find('p')
-1
>>> # 문자가 없을경우 -1을 출력
>>> a.inedx('y')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.inedx('y')
AttributeError: 'str' object has no attribute 'inedx'. Did you mean: 'index'?
>>> a.index('y')
1
>>> a.index('p')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.index('p')
ValueError: substring not found
>>> 
>>> b = ","
>>> c = b.join('Abcd')
>>> c
'A,b,c,d'
>>> a.upper()
'PYTHON'
>>> a.lower()
'python'
>>> 
>>> d = "    py    "
>>> d.lstrip()
'py    '
>>> d.rstrip()
'    py'
>>> d.strip()
'py'
>>> # 순서대로 왼쪽 공백 제거, 오른쪽 공백 제거, 전체 공백 제거
>>> 
>>> # 문자열 수정은 불가능
>>> a = 'Pithon'
>>> a[1] = 'y'
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a[1] = 'y'
TypeError: 'str' object does not support item assignment
>>> 
>>> a = "Python is difficult."
>>> a.replace("difficult", "funny")
'Python is funny.'
