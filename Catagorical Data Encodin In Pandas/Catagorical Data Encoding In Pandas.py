#Encode categorical Data in Pandas
from sklearn.preprocessing import LabelEncoder
import pandas as pd
df = pd.read_csv("D:\Python Courses\sample_data.csv")
df_lable = df.copy()

le = LabelEncoder()
df_lable["Gender_Encoder"] = le.fit_transform(df_lable['Gender'])
df_lable["Passed_Encoder"] = le.fit_transform(df_lable['Passed'])
print(df_lable)
# print(df["Passed"].value_counts())

#print(df_lable[["Name","Gender","Gender_Encoder","Passed","Passed_Encoder"]].head(5))

df_encode = pd.get_dummies(df, columns=["City"],dtype=int) #This is one-hot Encoding #Ye ek Pandas function hai. Iska kaam hai Categorical (text) data ko numbers (0 aur 1) mein convert karna.
print(df_encode)

#one hot encoding city k column ko khatam kr dy ga or os k alag sy 3 colulumns bnaa dy ga


