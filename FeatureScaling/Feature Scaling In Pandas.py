#Feature Scaling in Pandas
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split #ye skit-learn ka module hai jiska kaam hai data ko train aur test mein split karna
data = {
    'StudyHours':[1,2,3,4,5],
    'TestScore':[40,50,60,70,80]
}
df = pd.DataFrame(data)

standard_scaler = StandardScaler()
standard_scaled = standard_scaler.fit_transform(df)
print(pd.DataFrame(standard_scaled,columns=['StudyHours','TestScore']))
minmax_scaler = MinMaxScaler()
minmax_scaled = minmax_scaler.fit_transform(df)
print(pd.DataFrame(minmax_scaled,columns=['StudyHours','TestScore']))