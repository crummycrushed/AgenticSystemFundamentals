import pandas as pd
import matplotlib.pyplot as plt

data = {
    "day": [1, 2, 3, 4,5],
    "users": [120, 150, 170, 160, 180],
    "purchases": [30, 35, 40, 38, 45]
}


df = pd.DataFrame(data)


# Do more users lead to more purchases ?

plt.scatter(df["users"], df["purchases"])
plt.xlabel("Users")
plt.ylabel("Purchases")
plt.title("Users vs Purchases")

plt.show()