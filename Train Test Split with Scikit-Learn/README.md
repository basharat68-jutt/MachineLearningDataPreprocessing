# Train Test Split with Scikit-Learn

This project demonstrates how to split a dataset into **training data** and **testing data** using `train_test_split()` from Scikit-Learn.

## 📌 About

In Machine Learning, we usually divide our dataset into two parts:

* **Training Data:** Used to train the Machine Learning model.
* **Testing Data:** Used to evaluate how well the model performs on unseen data.

In this example, we have a small dataset containing **Study Hours** and **Test Scores**. The dataset is divided into training and testing sets using `train_test_split()`.

## 🛠️ Libraries Used

* **Pandas** – Used to create and work with the DataFrame.
* **Scikit-Learn** – Used for splitting the data into training and testing sets.

## 📊 Dataset

The dataset contains two columns:

| Column       | Description                       |
| ------------ | --------------------------------- |
| `StudyHours` | Number of hours a student studied |
| `TestScore`  | Score obtained by the student     |

Example:

```text
StudyHours    TestScore
1             40
2             50
3             60
4             70
5             80
```

## 🔄 Train Test Split

The following code is used to split the data:

```python
x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    random_state=42
)
```

### Parameters

**`test_size=0.2`**

It means **20% of the data is kept for testing**, while the remaining **80% is used for training**.

Since this dataset contains 5 rows:

* Training data → 4 rows
* Testing data → 1 row

**`random_state=42`**

It makes the split reproducible. This means that whenever the code is run again, the same rows will be selected for training and testing.

## 🎯 X and Y

In this example:

```python
x = df[['StudyHours']]
y = df[['TestScore']]
```

* `x` → Input/feature used by the Machine Learning model.
* `y` → Target/output that the model will learn to predict.

## 📤 Output

The program prints:

* Training features (`x_train`)
* Testing features (`x_test`)
* Training target (`y_train`)
* Testing target (`y_test`)

This helps understand which data will be used for training and which data will be used for testing.

## 🚀 Key Learning

Through this project, I learned:

* How to create a DataFrame using Pandas.
* How to separate features (`X`) and target (`Y`).
* How to use `train_test_split()`.
* What `test_size` means.
* Why `random_state` is used.
* The difference between training and testing data.

## 📚 Conclusion

Splitting data into training and testing sets is an important step in a Machine Learning workflow. The model learns from the training data and is then evaluated using the testing data to check its performance on unseen data.
