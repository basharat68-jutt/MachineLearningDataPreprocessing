"""Logistic Regression Practice Program"""

"""only two outputs 0 or 1"""

from sklearn.linear_model import LogisticRegression
x = [[1],[2],[3],[4],[5]]
y = [0,0,1,1,1]

model = LogisticRegression()
model.fit(x,y)
hours = float(input("Enter how many hours you studies = "))
result = model.predict([[hours]])[0] #ho skta hai k output array([1]) ay to [0] os k 1st element mtlab 1 ko nikaal k dy ga
if result == 1:
    print(f"Based on hours {hours}, you are likely to Pass")
else:
    print(f"Based on hours {hours}, you are likely to Fail")
