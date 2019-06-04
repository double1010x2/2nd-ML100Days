import numpy as np
import matplotlib.pyplot as plt

w = 3
b = 0.5
x_lin = np.linspace(0, 100, 101)
y = (x_lin + np.random.randn(101)*5)*w+b
y_hat = x_lin * w + b
MSE   = np.mean((y-y_hat)**2)

plt.plot(x_lin, y_hat, 'r-', label='predition')
plt.plot(x_lin, y, 'b.', label='data points')
plt.title('Assume we have data points')
plt.legend(loc=2)
plt.show()
