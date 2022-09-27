import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv("./files/xn.txt", header = None)
y = pd.read_csv("./files/yn.txt", header = None)

plt.subplot(2, 1, 1)
plt.stem(range(0,6),x)
plt.title('Digital Filter Input-Output')
plt.ylabel('$x(n)$')
plt.grid()

plt.subplot(2, 1, 2)
plt.stem(range(0,20),y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()

plt.savefig('./figs/ep20b11011_xnyn.pdf')
plt.savefig('./figs/ep20b11011_xnyn.eps')