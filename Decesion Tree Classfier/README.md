# Decision Tree Classifier 🌳

This is a beginner-level **Machine Learning classification project** using the `DecisionTreeClassifier` from Scikit-learn.

The model learns from fruit data and predicts whether a fruit is likely an **Apple** or an **Orange** based on its:

* Size/weight in grams
* Shade value

## 📌 What is a Decision Tree?

A **Decision Tree** is a supervised machine learning algorithm used for **classification and regression**.

For classification, the tree makes decisions by asking questions about the input features and eventually reaches a prediction.

For example:

```text
Is size <= 8.5?
      /       \
    Yes       No
    Apple    Orange
```

The actual decision rules are automatically learned from the training data.

## 📊 Dataset

The example uses two features:

| Size | Shade | Fruit  |
| ---- | ----- | ------ |
| 7    | 2     | Apple  |
| 8    | 3     | Apple  |
| 9    | 8     | Orange |
| 10   | 9     | Orange |

The target values are:

```python
y = [0, 0, 1, 1]
```

Where:

* `0` = Apple
* `1` = Orange

## ⚙️ How the Code Works

### 1. Import Decision Tree

```python
from sklearn.tree import DecisionTreeClassifier
```

This imports the `DecisionTreeClassifier` from Scikit-learn.

### 2. Create Training Data

```python
x = [
    [7, 2],
    [8, 3],
    [9, 8],
    [10, 9]
]

y = [0, 0, 1, 1]
```

`x` contains the input features, while `y` contains the labels.

### 3. Create the Model

```python
model = DecisionTreeClassifier()
```

This creates a Decision Tree classification model.

### 4. Train the Model

```python
model.fit(x, y)
```

The model learns the relationship between the fruit features and their labels.

### 5. Take User Input

```python
size = float(input("Enter the fruit size in grams: "))
shade = float(input("Enter fruit shade in cm: "))
```

The user provides the size and shade of a new fruit.

### 6. Make a Prediction

```python
result = model.predict([[size, shade]])[0]
```

The trained model predicts whether the fruit belongs to class `0` or `1`.

### 7. Display the Result

```python
if result == 0:
    print("This is likely an Apple.")
else:
    print("This is likely an Orange.")
```

The numerical prediction is converted into a meaningful fruit name.

## 🧠 Example

If the user enters:

```text
Enter the fruit size in grams: 8
Enter fruit shade in cm: 3
```

The model may predict:

```text
This is likely an Apple.
```

If the user enters:

```text
Enter the fruit size in grams: 10
Enter fruit shade in cm: 9
```

The model may predict:

```text
This is likely an Orange.
```

## 🛠️ Technologies Used

* Python
* Scikit-learn
* Decision Tree Classification

## 🎯 Learning Goals

This practice helped me understand:

* Decision Tree Classification
* Features and labels
* Model training using `.fit()`
* Making predictions using `.predict()`
* Converting numerical predictions into meaningful output
* Basic supervised machine learning

## 📌 Note

This is a **small practice dataset** created for learning purposes. A real-world machine learning model would require a larger and more diverse dataset, along with proper training/testing and model evaluation.
