import matplotlib.pyplot as plt
import numpy as np
import time

x = np.linspace(0, 10, 50)

weight = 0.2

plt.ion()

fig, ax = plt.subplots()

for step in range(40):
    prediction = weight * x

    ax.clear()
    ax.plot(x, prediction)

    ax.set_title(f"Live Prediction | weight = {weight: .2f}")
    ax.set_xlabel("Input (x)")
    ax.set_ylabel("Prediction")

    plt.draw()
    plt.pause(0.2)

    weight += 0.05

plt.ioff()
plt.show()