Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
pd.__version__
'2.2.2'

# series 생성
data1 = [10, 20, 30, 40, 50]
data1
[10, 20, 30, 40, 50]
data2 = ['1반', '2반', '3반', '4반', '5반']
data2
['1반', '2반', '3반', '4반', '5반']

# 리스트를 이용하여 생성
sr1 = pd.Series(data1)
sr1
0    10
1    20
2    30
3    40
4    50
dtype: int64
sr2 = pd.Series(data2)
sr2
0    1반
1    2반
2    3반
3    4반
4    5반
dtype: object

# 값을 이용하여 생성
sr3 = pd.Series([101, 102, 103, 104, 105])
sr3
0    101
1    102
2    103
3    104
4    105
dtype: int64
sr4 = pd.Series(['월', '화', '수', '목', '금'])
sr4
0    월
1    화
2    수
3    목
4    금
dtype: object

# 인덱스를 지정하여 생성
sr5 = pd.Series(data1, index = [1000, 1001, 1002, 1003, 1004])
sr5
1000    10
1001    20
1002    30
1003    40
1004    50
dtype: int64
sr6 = pd.Series(data1, index = data2)
sr6
1반    10
2반    20
3반    30
4반    40
5반    50
dtype: int64
sr7 = pd.Series(data2, index = data1)
sr7
10    1반
20    2반
30    3반
40    4반
50    5반
dtype: object
sr8 = pd.Series(data2, index = sr4)
sr8
월    1반
화    2반
수    3반
목    4반
금    5반
dtype: object

# Series 인덱싱
sr8[2]

Warning (from warnings module):
  File "<pyshell#32>", line 1
FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`
'3반'
>>> sr8['수']
'3반'
>>> sr8[-1]
'5반'
>>> 
>>> # Series 슬라이싱
>>> sr8[0:4]
월    1반
화    2반
수    3반
목    4반
dtype: object
>>> 
>>> # 인덱스 구하기
>>> sr8.index
Index(['월', '화', '수', '목', '금'], dtype='object')
>>> 
>>> # 값 구하기
>>> sr8.values
array(['1반', '2반', '3반', '4반', '5반'], dtype=object)
>>> 
>>> # 더하기
>>> sr1 + sr3
0    111
1    122
2    133
3    144
4    155
dtype: int64
>>> sr4 + sr2
0    월1반
1    화2반
2    수3반
3    목4반
4    금5반
dtype: object
