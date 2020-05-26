import matplotlib.pyplot as plt
import numpy as np

# 누적 막대 그래프 그리기

# np.random.rand(m, n) : 0 ~ 1의 표준정규분포 난수를 matrix array(m, n) 생성
x = np.random.rand(10) # 아래 막대
y = np.random.rand(10) # 중간 막대
z = np.random.rand(10) # 위 막대
data = [x, y, z]
x_array = np.arange(10) # X의 위치를 0~ 9까지 설정한 것
for i in range(0, 3): # 누적 막대의 종류가 3개
    plt.bar(
        x_array, # 0부터 10까지의 X 위치에서
        data[i], # 각 높이 (10개)만큼 쌓음
        bottom=np.sum(data[:i], axis=0)
    )
plt.show()