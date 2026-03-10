import pandas as pd
import matplotlib.pyplot as plt

data = {
    "day": [1, 2, 3, 4,5],
    "users": [120, 150, 170, 160, 180],
    "purchases": [30, 35, 40, 38, 45]
}


df = pd.DataFrame(data)

#print(df)

#plt.figure(figsize=(10,4)) #1 image


#plt.subplot(2, 3, 1)
plt.plot(df["day"], df["users"])
plt.xlabel("Day")
plt.ylabel("Number of Users")
plt.title("App users over Time")


# Are purchases increasing over time ?


#plt.subplot(2, 3, 4)
plt.plot(df["day"], df["purchases"])
plt.xlabel("Day")
plt.ylabel("Number of purchases")
plt.title("Purchases per day")



plt.show()