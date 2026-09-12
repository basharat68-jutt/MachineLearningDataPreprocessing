#Handling Missing Data in Pandas
import pandas as pd
data = {
    'Name':['pavan','Kapil','Lalit','Ishan','Om'],
    'Age':[25,None,44,23,None],
    'Salary':[50000,60000,70000,None,None]
}
df = pd.DataFrame(data)
print(df)
print(df.isnull().sum())
df_drop = df.dropna()
print(df_drop)
df["Age"] = df["Age"].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print(df)
