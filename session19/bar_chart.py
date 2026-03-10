
import matplotlib.pyplot as plt


models = ["1", "2", "3"]
sales = [20, 1, 12]

plt.bar(models, sales)

plt.xlabel("Model")
plt.ylabel("Sales")
plt.title("Model Comparison")

plt.show()