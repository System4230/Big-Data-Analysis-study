# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

data1 = [10, 20, 30, 40, 50]
data2 = ['1반','2반','3반','4반','5반']

# pd.DataFrame() 형식
data_dic = {'year' : [2018, 2019, 2020], 'sales' : [350, 480, 1099]}
data_dic

# 딕셔너리를 이용하여 생성
df1 = pd.DataFrame(data_dic)
df1

# 리스트를 이용하여 생성
df2 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]],
                   index = ['중간고사', '기말고사'], columns = data2[0:3])
df2

data_df = [['20201101', 'Hong', '90', '95'], ['20201102', 'Kim', '93', '94'], ['20201103', 'Lee', '87', '97']]
df3 = pd.DataFrame(data_df)
df3

# 열 이름 설정
df3.columns = ['학번', '이름', '중간고사', '기말고사']
df3

# 조회
df3.head(2)
df3.tail(2)
df3['이름']