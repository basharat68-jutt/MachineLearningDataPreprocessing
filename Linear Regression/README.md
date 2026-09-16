# Linear Regression

This project is a beginner-friendly implementation of **Linear Regression** using Python and Scikit-learn.

## 📌 About Linear Regression

Linear Regression is a supervised machine learning algorithm that finds a relationship between input data and output data.

It tries to find a **best-fit straight line** through the data and uses that line to make predictions.

In this example:

* **Input (X)** = Study Hours
* **Output (Y)** = Marks
* The model learns the relationship between study hours and marks.
* After training, the user enters study hours and the model predicts the expected marks.

The basic idea of a linear equation is:

**y = mx + b**

Where:

* `y` = predicted output
* `x` = input
* `m` = slope
* `b` = intercept

## 📊 Dataset

The example uses a small dataset:

| Study Hours | Marks |
| ----------: | ----: |
|           1 |    40 |
|           2 |    50 |
|           3 |    65 |
|           4 |    75 |
|           5 |    90 |

Only a few rows are used because this is a learning/practice example.

## 🛠️ Libraries Used

* Python
* Scikit-learn

## 🔄 How the Code Works

### 1. Import Linear Regression

```python
from sklearn.linear_model import LinearRegression
```

Imports the `LinearRegression` algorithm from Scikit-learn.

### 2. Create Input Data

```python
x = [[1],[2],[3],[4],[5]]
```

`x` contains the number of study hours.

The values are written as a **2D list** because Scikit-learn expects input features in this format.

### 3. Create Output Data

```python
y = [40,50,65,75,90]
```

`y` contains the marks corresponding to the study hours.

### 4. Create the Model

```python
model = LinearRegression()
```

Creates a Linear Regression model.

### 5. Train the Model

```python
model.fit(x,y)
```

The model learns the relationship between study hours and marks from the provided data.

### 6. Take User Input

```python
hours = float(input("Enter how many hours you studies = "))
```

The user enters the number of hours studied.

### 7. Make Prediction

```python
predicted_marks = model.predict([[hours]])
```

The trained model predicts the marks for the entered study hours.

### 8. Display Result

```python
print(f"Based on your hours {hours} you may scored arround {predicted_marks}")
```

Displays the predicted marks.

## 💡 Important Learning Points

### 1. It's not only about the line

Machine learning is not just about getting numbers from a model. We should also understand what those predictions mean in the real-world context.

### 2. Start with a small dataset

For learning and understanding the algorithm, a small dataset is useful. Once the concept is clear, larger and real-world datasets can be used.

### 3. Accuracy is not always the goal

For Regression problems, accuracy is generally **not the main evaluation metric** like it is in classification.

Metrics such as:

* MAE
* MSE
* RMSE
* R² Score

are commonly used to evaluate regression models.

The goal is to understand the model and improve the quality of its predictions.

## 🎯 Project Goal

The main goal of this project is to understand the basic workflow of Linear Regression:

**Data → Model → Training → User Input → Prediction**

## 🚀 Future Improvements

* Add more training data
* Visualize the data and regression line
* Calculate MAE, MSE and R² Score
* Compare predicted values with actual values
* Use a real-world dataset
