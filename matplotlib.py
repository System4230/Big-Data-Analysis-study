# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 03:13:30 2024

@author: v
"""

import matplotlib
matplotlib.__version__
import matplotlib.pyplot as plt

# 데이터 준비
x = [2016, 2017, 2018, 2019, 2020]
y = [350, 410, 520, 695, 543]

# x축과 y축을 지정하여 라인플롯 생성
plt.plot(x,y)

# 차트 제목 설정
plt.title('Annual sales')

# x축 레이블 설정
plt.xlabel('years')

# y축 레이블 설정
plt.ylabel('sales')

# 라인플롯 표시
plt.show()


# 바 차트 그리기
# 데이터 준비
y1 = [350, 410, 520, 695]
y2 = [200, 250, 385, 350]
x = range(len(y1))

# x축과 y축을 지정하여 바차트 생성
plt.bar(x, y1, width = 0.7, color = "blue")
plt.bar(x, y2, width = 0.7, color = "red", bottom = y1)

# 차트 제목 설정
plt.title('Quarterly sales')

# x축 레이블 설정
plt.xlabel('Quarters')

# y축 레이블 설정
plt.ylabel('sales')

# 눈금 이름 리스트 생성
xLabel = ['First', 'second', 'third', 'fourth']

# 바 차타의 x축 눈금 이름 설정
plt.xticks(x, xLabel, fontsize = 10)

# 범례 설정
plt.legend(['chairs', 'desks'])

# 바 차트 표시
plt.show()