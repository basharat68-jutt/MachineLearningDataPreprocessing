# Logistic Regression Practice Program

This is a beginner-level Machine Learning practice program using **Logistic Regression** from Scikit-learn.

## 📌 About the Project

Logistic Regression is a classification algorithm used when the output has two possible classes, such as:

* `0` → Fail
* `1` → Pass

In this program, the model learns the relationship between **study hours** and whether a student **Passes or Fails**.

## 🧠 Dataset

The program uses a small sample dataset:

```python
x = [[1], [2], [3], [4], [5]]
y = [0, 0, 1, 1, 1]
```

Here:

* `x` = Number of study hours
* `y` = Result
* `0` = Fail
* `1` = Pass

For example:

| Study Hours |   Result |
| ----------: | -------: |
|           1 | 0 (Fail) |
|           2 | 0 (Fail) |
|           3 | 1 (Pass) |
|           4 | 1 (Pass) |
|           5 | 1 (Pass) |

## ⚙️ How It Works

1. Import `LogisticRegression` from Scikit-learn.
2. Create training data containing study hours and results.
3. Create a Logistic Regression model.
4. Train the model using `model.fit(x, y)`.
5. Ask the user to enter study hours.
6. Use `model.predict()` to predict the result.
7. Display whether the student is likely to Pass or Fail.

## 🔑 Important Code

```python
model = LogisticRegression()

model.fit(x, y)

hours = float(input("Enter how many hours you studies = "))

result = model.predict([[hours]])[0]
```

`model.predict()` returns an array, for example:

```python
[1]
```

Using `[0]` gets the first element from that array:

```python
result = model.predict([[hours]])[0]
```

So `result` becomes:

```text
1
```

or

```text
0
```

## 📊 Example

If the user enters:

```text
Enter how many hours you studies = 4
```

The output may be:

```text
Based on hours 4.0, you are likely to Pass
```

If the user enters fewer hours, the model may predict:

```text
Based on hours 1.0, you are likely to Fail
```

## 🛠️ Technologies Used

* Python
* Scikit-learn
* Logistic Regression

## 🎯 Learning Objectives

Through this practice program, I learned:

* What Logistic Regression is
* Binary classification (`0` and `1`)
* Training a classification model
* Using `model.fit()`
* Using `model.predict()`
* Taking user input for prediction
* Converting model output into a simple Pass/Fail result
