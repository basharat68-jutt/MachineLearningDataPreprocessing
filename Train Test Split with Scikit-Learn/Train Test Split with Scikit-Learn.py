import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split #ye skit-learn ka module hai jiska kaam hai data ko train aur test mein split karna
data = {
    'StudyHours':[1,2,3,4,5],
    'TestScore':[40,50,60,70,80]
}
df = pd.DataFrame(data)

x = df[['StudyHours']]
y = df[['TestScore']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
#sb sy phly function dekhta hai test_size k kitna data testing k leye rkhna hai


print("Training Data")
print(x_train)
print("Test Data")
print(x_test)
print("Training Data")
print(y_train)
print("Test Data")
print(y_test)