# Feature Scaling in Pandas

This project demonstrates **Feature Scaling** using Pandas and Scikit-learn.

Feature scaling is an important preprocessing step in Machine Learning. It brings numerical features to a similar scale so that features with larger values do not dominate the model.

## 📌 What is Feature Scaling?

Feature Scaling is the process of transforming numerical features into a common scale.

For example:

* `StudyHours` → values from 1 to 5
* `TestScore` → values from 40 to 80

The ranges of these features are different, so scaling can make them more comparable.

## 🛠️ Libraries Used

* **Pandas** → For creating and working with the DataFrame
* **Scikit-learn** → For feature scaling
* **StandardScaler** → Performs Standardization
* **MinMaxScaler** → Performs Min-Max Scaling

## 📊 Dataset

The example dataset contains two features:

| StudyHours | TestScore |
| ---------: | --------: |
|          1 |        40 |
|          2 |        50 |
|          3 |        60 |
|          4 |        70 |
|          5 |        80 |

## 1️⃣ StandardScaler

`StandardScaler` standardizes the features so that they have approximately:

* Mean = `0`
* Standard Deviation = `1`

```python
standard_scaler = StandardScaler()
standard_scaled = standard_scaler.fit_transform(df)
```

The scaled values are then converted back into a DataFrame for better readability.

```python
print(pd.DataFrame(
    standard_scaled,
    columns=['StudyHours','TestScore']
))
```

### Formula

```text
z = (x - mean) / standard_deviation
```

## 2️⃣ MinMaxScaler

`MinMaxScaler` scales the values into a specified range. By default, the range is:

```text
0 to 1
```

```python
minmax_scaler = MinMaxScaler()
minmax_scaled = minmax_scaler.fit_transform(df)
```

The result is again converted into a DataFrame:

```python
print(pd.DataFrame(
    minmax_scaled,
    columns=['StudyHours','TestScore']
))
```

### Formula

```text
x_scaled = (x - min(x)) / (max(x) - min(x))
```

## 🔍 StandardScaler vs MinMaxScaler

| StandardScaler                             | MinMaxScaler                     |
| ------------------------------------------ | -------------------------------- |
| Mean becomes approximately 0               | Minimum becomes 0                |
| Standard deviation becomes approximately 1 | Maximum becomes 1                |
| Uses mean and standard deviation           | Uses minimum and maximum         |
| Values are not restricted to 0–1           | Values are generally between 0–1 |

## 🎯 Why Feature Scaling is Important?

Feature scaling is especially useful for Machine Learning algorithms that are sensitive to the magnitude of features.

It can be important for algorithms such as:

* K-Nearest Neighbors (KNN)
* K-Means Clustering
* Support Vector Machine (SVM)
* Logistic Regression
* Linear Regression
* Neural Networks
* Gradient-based algorithms

## ⚠️ Important Note

In a real Machine Learning project, the scaler should generally be **fitted only on the training data** and then used to transform the test data.

Example:

```python
X_train, X_test = train_test_split(df, test_size=0.2, random_state=42)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

Here:

* `fit_transform()` → learns the scaling parameters from training data and transforms it.
* `transform()` → uses the already learned parameters to transform test data.

This helps prevent **data leakage**.

## 📚 Learning Objective

The main purpose of this practice is to understand:

* What Feature Scaling is
* Why Feature Scaling is used in Machine Learning
* How `StandardScaler` works
* How `MinMaxScaler` works
* Difference between Standardization and Min-Max Scaling
* Basic use of `fit_transform()` and `transform()`
* Importance of avoiding data leakage

## 👨‍💻 Author

Basharat Jutt
