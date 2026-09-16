"""
***Linear Regression***

1-finds a pattern in old data
2-straight line
3-line
y = mx+b
[[value]] 2d list
[[6]]

x = [[1],[2],[3],[4],[5]]

Remember three things
1- its not about the line, its about the story(dont trust only on numbers see output according your mind)
2- 5 rows use start
3- accuracy is not always the goal (make output better than previous)

"""
from sklearn.linear_model import LinearRegression
x = [[1],[2],[3],[4],[5]]
y = [40,50,65,75,90]
model = LinearRegression()
model.fit(x,y)
hours = float(input("Enter how many hours you studies = "))

predicted_marks = model.predict([[hours]])
print(f"Based on your hours {hours} you may scored arround {predicted_marks}")