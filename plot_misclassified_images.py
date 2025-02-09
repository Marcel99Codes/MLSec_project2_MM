import matplotlib.pyplot as plt

iterations = [1, 3, 10, 20]
values = [18, 20, 21, 22]

plt.plot(iterations, values, marker='o')
plt.xlabel('Iterations')
plt.ylabel('Amount of Images')
plt.title('Misclassified Images over Iterations')
plt.ylim(0, 100)
plt.grid(True)
plt.show()
