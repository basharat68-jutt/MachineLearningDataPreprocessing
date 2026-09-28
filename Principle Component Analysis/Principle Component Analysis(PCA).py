"""PCA"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA #decomposition means kuch bohat bada jis ko hm choty parts mein tor rhyy hain

data = {
    "Age" : [25,30,35,40,45,50],
    "Income" : [30000,40000,50000,60000,70000,80000],
    "Spending" : [70,60,50,40,30,20],
    "Savings" : [1000,5000,8000,10000,15000,20000]
}

df = pd.DataFrame(data)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
# print(scaled_data) 
# date = pd.DataFrame(scaled_data)
# print(date)

pca = PCA(n_components=2) #n_componenets means k jo data hai osko 2 mein shrink k lena hai
pca_result = pca.fit_transform(scaled_data)

pca_df = pd.DataFrame(pca_result, columns=["PCA1","PCA2"])

explained_varience = pca.explained_variance_ratio_  #kitna percentage of total information hr component pr captured hoa hai...ye sirg ye dikhaye ga k kitna 2no columns ny kitni kitni information li hoe hai
print("Variance captured by each PCA component.")
print(np.round(explained_varience * 100,2))

plt.figure(figsize=(8,6))
plt.scatter(pca_df["PCA1"], pca_df["PCA2"], color = "black" )
plt.title("PCA Projection (2D View)")
plt.xlabel("PCA Main Pattern")
plt.ylabel("PCA Minor Pattern")
plt.grid(True)
plt.show()
print("New data with 2 features PCA1 PCA2")
print(pca_df)