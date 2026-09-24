""" MAE(Mean Absolute Error)
1- take the mistake difference
2- remove the minus sign
3- add all mistake
4- devide by all students
use kro jb simple answer chahiyye k mera model average kitni galti kr rhaa hai
"""

"""MSE(Mean Squared Error)
mistakes kok add kr dein gy or sbhi ko or bda bnaa dy gein
first square all mistakes numbers and then sum them and divide by total
MSC badi mistakes jin ko kafi strong treeky sy calculate kia jata hai
jb badi mistake ko bdyy pemaany pr dekhna ho
"""

"""RMSE(Root Mean Square Error)
square root of MSC
show in normal units like marks
jb ye smjhna ho k real units mein kia error a rhaa hai
"""
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
#real score
real_score = [90, 60, 80, 100]

#model guess
predicted_score = [85, 70, 70 ,95]

mae = mean_absolute_error(real_score,predicted_score)
mse = mean_squared_error(real_score,predicted_score)
rmse = np.sqrt(mse)
print("MAE: On average off by",mae)
print("MSE: Squard Mistake value",mse)
print("RMSE: Final Realistic error",rmse)



