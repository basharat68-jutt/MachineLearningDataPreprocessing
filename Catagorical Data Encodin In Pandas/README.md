# Categorical Data Encoding in Pandas

This project demonstrates how to convert **categorical (text) data into numerical data** using Pandas and Scikit-learn.

Machine Learning algorithms generally work with numerical values, so categorical columns such as `Gender`, `Passed`, and `City` need to be converted into numbers.

## 📌 Concepts Covered

* Label Encoding
* One-Hot Encoding
* Converting categorical data into numerical data
* Using `LabelEncoder`
* Using Pandas `get_dummies()`

---

## 📂 Dataset

The project uses a sample CSV dataset:

```text
sample_data.csv
```

The dataset contains categorical columns such as:

* `Gender`
* `Passed`
* `City`

---

## 1. Label Encoding

Label Encoding converts each category into a numerical value.

For example:

```text
Gender

Male    → 1
Female  → 0
```

In the code:

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df_lable["Gender_Encoder"] = le.fit_transform(df_lable["Gender"])
df_lable["Passed_Encoder"] = le.fit_transform(df_lable["Passed"])
```

### How it works

`LabelEncoder()` creates numerical labels for the unique categories.

```python
le.fit_transform()
```

performs two operations:

* `fit()` → finds the unique categories
* `transform()` → converts those categories into numbers

The encoded values are stored in new columns:

```text
Gender_Encoder
Passed_Encoder
```

The original columns are kept as well.

---

## 2. One-Hot Encoding

One-Hot Encoding converts a categorical column into multiple numerical columns containing `0` and `1`.

For example, if the `City` column contains:

```text
Lahore
Islamabad
Karachi
```

One-Hot Encoding creates separate columns:

```text
City_Lahore
City_Islamabad
City_Karachi
```

The values indicate whether a row belongs to that category:

```text
City_Lahore    City_Islamabad    City_Karachi
     1                0                0
     0                1                0
     0                0                1
```

In the code:

```python
df_encode = pd.get_dummies(
    df,
    columns=["City"],
    dtype=int
)
```

### Important

`pd.get_dummies()` is a **Pandas function** used for One-Hot Encoding.

It removes the original `City` column and creates separate columns for its categories.

---

## 🔄 Label Encoding vs One-Hot Encoding

| Label Encoding                       | One-Hot Encoding              |
| ------------------------------------ | ----------------------------- |
| Converts categories into numbers     | Creates separate columns      |
| Usually creates one encoded column   | Creates multiple columns      |
| Example: Male → 1, Female → 0        | Example: City_Lahore → 1/0    |
| Useful for binary/ordinal categories | Useful for nominal categories |
| Uses `LabelEncoder`                  | Uses `pd.get_dummies()`       |

---

## 🧠 Example

Suppose we have:

```text
Gender
------
Male
Female
Male
```

Label Encoding can produce:

```text
Gender    Gender_Encoder
Male            1
Female          0
Male            1
```

For a `City` column:

```text
City
------
Lahore
Karachi
Islamabad
```

One-Hot Encoding produces:

```text
City_Lahore    City_Karachi    City_Islamabad
     1              0                0
     0              1                0
     0              0                1
```

---

## 🛠️ Libraries Used

* **Pandas** → Reading and manipulating the dataset and performing One-Hot Encoding
* **Scikit-learn** → Performing Label Encoding

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder
```

---

## 🎯 Learning Outcome

After completing this project, you will understand:

* What categorical data is
* Why categorical data needs encoding
* How Label Encoding works
* How One-Hot Encoding works
* How to use `LabelEncoder`
* How to use Pandas `get_dummies()`
* The difference between Label Encoding and One-Hot Encoding

---

## 🚀 Conclusion

Categorical data must often be converted into numerical form before it can be used in Machine Learning models.

In this project:

**Label Encoding** was used for `Gender` and `Passed`, while **One-Hot Encoding** was used for the `City` column.

These techniques are important preprocessing steps in a typical Machine Learning workflow.
