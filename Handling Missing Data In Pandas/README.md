# Handling Missing Data in Pandas

## 📌 Overview

This project demonstrates how to **identify and handle missing values** in a dataset using **Pandas**.

Handling missing data is an important step in **Machine Learning data preprocessing**, because many ML algorithms cannot work properly when the dataset contains `NaN` or missing values.

In this example, a small employee dataset is created containing **Name, Age, and Salary**.

---

## 🛠️ Technologies Used

* Python
* Pandas

---

## 📊 Dataset

The dataset contains the following columns:

| Column | Description     |
| ------ | --------------- |
| Name   | Employee name   |
| Age    | Employee age    |
| Salary | Employee salary |

Some values in the `Age` and `Salary` columns are intentionally set to `None` to demonstrate missing-value handling.

---

## 🔍 Checking Missing Values

Pandas provides the `isnull()` function to identify missing values.

```python
print(df.isnull().sum())
```

* `isnull()` checks whether a value is missing.
* `sum()` counts the number of missing values in each column.

This helps us understand where missing data exists before applying any ML model.

---

## 🗑️ Removing Missing Values

We can remove rows containing missing values using `dropna()`:

```python
df_drop = df.dropna()

print(df_drop)
```

`dropna()` removes rows that contain at least one missing value.

### ⚠️ Important

Dropping rows can result in losing useful data. Therefore, it should not always be the first choice, especially when the dataset is large.

---

## 🔢 Filling Missing Values

Instead of deleting rows, missing numerical values can be replaced with a statistical value such as the **mean**.

### Age

```python
df["Age"] = df["Age"].fillna(df["Age"].mean())
```

Here:

* `df["Age"].mean()` calculates the average age.
* `fillna()` replaces missing values with that average.

### Salary

```python
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
```

The same method is used to replace missing salary values with the average salary.

---

## 🧠 Why Is This Important for Machine Learning?

Real-world datasets often contain missing values.

For example:

```text
Age      Salary
25       50000
NaN      60000
44       70000
23       NaN
NaN      NaN
```

Before training a Machine Learning model, these missing values usually need to be handled.

Common techniques include:

* Removing rows using `dropna()`
* Removing columns when appropriate
* Filling values using mean
* Filling values using median
* Filling categorical values using mode
* Using more advanced imputation techniques

---

## 🎯 Key Learning

From this project, I learned:

* How to create a DataFrame using Pandas
* How to identify missing values using `isnull()`
* How to count missing values using `sum()`
* How to remove missing values using `dropna()`
* How to replace missing values using `fillna()`
* How mean imputation can be used for numerical data
* Why missing-value handling is important before Machine Learning

---

## 🚀 Machine Learning Connection

**Missing Value Handling → Data Preprocessing → Feature Preparation → Model Training**

This is one of the first steps in preparing real-world data for Machine Learning.
