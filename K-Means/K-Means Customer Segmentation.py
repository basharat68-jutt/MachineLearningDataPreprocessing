"""K-Means"""

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#Sample Data
data = {
    "Customer" : ['Riya',"Aman","Faizan","Neha","Imran","Sneh"],
    "Age" : [20,30,40,22,38,25],
    "Spending" : [100,200,300,110,290,130]
    }

df = pd.DataFrame(data)

x = df[["Age","Spending"]]
model = KMeans(n_clusters=2, random_state=42, n_init=10) #yaha 2 clusters bnaa diye hain ab bs  predict krna hai
df["Group"] = model.fit_predict(x) #__ye her 1 row k leye group number dy ga k ye customer group 0 mein jaye ga or ye group 1 mein jaye ga

plt.figure(figsize=(6,5))
for group in df["Group"].unique():
    group_data = df[df["Group"]==group]
    plt.scatter(group_data["Age"], group_data["Spending"], label=f"Group {group}")

plt.xlabel("Age")
plt.ylabel("Spending")
plt.title("Customer Segments(K-Means)")
plt.legend()
plt.grid(True)
plt.show
print(df)