import matplotlib.pyplot as plt
import numpy as np

# PI * 10 너비에 500개의 점을 균일하게 찍기
x = np.linspace(0, np.pi * 10, 500)
# 2개의 그래프가 들어가는 Figure 생성; subplots(2, 1) : 2행 1열로 그래프 생성
fig, axes = plt.subplots(2, 1)
# 첫 번째 그래프는 사인(Sin) 그래프
axes[0].plot(x, np.sin(x))
# 두 번째 그래프는 코사인(Cos) 그래프
axes[1].plot(x, np.cos(x))
fig.savefig("sin&cos.png")