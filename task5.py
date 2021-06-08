import matplotlib.pyplot as plt
import math
import numpy as np

x = open("file.txt", "r")
x = x.read()
x = x.split(" ")
for i in range(100):
    x[i] = int(x[i])
y = list(range(1, 101))
for i in range(1, 99):
    y[i] = x[i] ** 2 + math.log(x[i] / 2)

# Plot the data
plt.plot(x, y, label='graph')

# Show the plot
plt.show()
