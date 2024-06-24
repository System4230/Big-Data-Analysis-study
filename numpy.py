Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
np.__version__
'2.0.0'

# 리스트를 이용하여 numpy 생성
ar1 = np.array([1, 2, 3, 4, 5])
ar1
array([1, 2, 3, 4, 5])
type(ar1)
<class 'numpy.ndarray'>
ar2 = np.array([[10, 20, 30], [40, 50, 60]])
ar2
array([[10, 20, 30],
       [40, 50, 60]])

# 값의 범위를 지정하여 numpy 생성
ar3 = np.arange(1, 11, 2)
ar3
array([1, 3, 5, 7, 9])

# 구조를 지정하여 numpy 생성
>>> ar4 = np.array([1, 2, 3, 4, 5, 6]).reshape((3,2))
>>> ar4
array([[1, 2],
       [3, 4],
       [5, 6]])
>>> 
>>> # 초기값과 구조를 지정하여 numpy 생성
>>> ar5 = np.zeros((2,3))
>>> ar5
array([[0., 0., 0.],
       [0., 0., 0.]])
>>> 
>>> # 슬라이싱
>>> ar6 = ar2[0:2, 0:2]
>>> ar6
array([[10, 20],
       [40, 50]])
>>> ar7 = ar2[0, :]
>>> ar7
array([10, 20, 30])
>>> 
>>> # 사칙연산
>>> ar8 = ar1 + 10
>>> ar8
array([11, 12, 13, 14, 15])
>>> ar1 + ar8
array([12, 14, 16, 18, 20])
>>> ar8 - ar1
array([10, 10, 10, 10, 10])
>>> ar1 * 2
array([ 2,  4,  6,  8, 10])
>>> ar1 / 2
array([0.5, 1. , 1.5, 2. , 2.5])
>>> 
>>> # 행렬곱
>>> ar9 = np.dot(ar2,ar4)
>>> ar9
array([[220, 280],
       [490, 640]])
