import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-9, 10)
y1 = x ** 2
y2 = -x
plt.plot(x, y1, linestyle="--", marker="*", color="red", label="y = x * x")
plt.plot(x, y2, linestyle=":", marker="o", color="blue", label="y = -x")
plt.xlabel("X")
plt.xlabel("Y")
# legend label의 대한 정보를 표현하는 것
# shadow : 음영, borderpad : 테두리
plt.legend(
    shadow=True,
    borderpad=1
)
plt.show()
