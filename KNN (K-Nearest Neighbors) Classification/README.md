# KNN (K-Nearest Neighbors) Classification

This is a simple machine learning practice program using the **K-Nearest Neighbors (KNN)** classification algorithm from Scikit-learn.

## 📌 What is KNN?

KNN stands for **K-Nearest Neighbors**.

It classifies a new data point by looking at the **nearest data points** from the training data and checking which class is most common among them.

In this project, KNN is used to predict whether a fruit is likely to be an:

* 🍎 Apple → `0`
* 🍊 Orange → `1`

## 📊 Input Features

The model uses two features:

* **Weight** — weight of the fruit in grams
* **Size** — size of the fruit in centimeters

Example training data:

```python
x = [
    [180, 7],
    [200, 7.5],
    [300, 8.5],
    [330, 9],
    [360, 9.5]
]
```

The target values are:

```python
y = [0, 0, 0, 1, 1]
```

Here:

* `0` represents Apple
* `1` represents Orange

## ⚙️ How the Model Works

The KNN model is created using:

```python
model = KNeighborsClassifier(n_neighbors=3)
```

`n_neighbors=3` means that the model looks at the **3 nearest training data points** when making a prediction.

Then the model is trained using:

```python
model.fit(x, y)
```

After training, the user enters the fruit's:

* Weight
* Size

The model predicts its class:

```python
prediction = model.predict([[weight, size]])[0]
```

## 🧠 Example

If the user enters:

```text
Enter the weight in grams: 340
Enter size in cm: 9
```

The model checks the nearest training examples and predicts the fruit class based on the majority of the 3 nearest neighbors.

## 🛠️ Technologies Used

* Python
* Scikit-learn
* K-Nearest Neighbors (KNN)

## 🎯 Learning Purpose

This project is created for practicing:

* KNN classification
* Training a machine learning model
* Using `KNeighborsClassifier`
* Taking user input
* Making predictions with a trained model
* Understanding nearest-neighbor based classification
