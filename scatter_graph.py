import matplotlib.pyplot as plt
import numpy as np

# 스캐터 그래프 그리기
# 데이터의 분산, 분포 등을 표현할 때 주로 사용

x = np.random.rand(10)
y = np.random.rand(10)
colors = np.random.randint(0, 100, 10)
sizes = np.pi * 1000 * np.random.rand(10)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.7)
plt.show()