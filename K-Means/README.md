# K-Means Customer Segmentation

This project is a simple practice of **K-Means Clustering** using Python and Scikit-learn.

## 📌 What is K-Means?

K-Means is an **unsupervised machine learning algorithm** used to divide data into different groups called **clusters**.

In this project, customers are grouped based on:

* **Age**
* **Spending**

The model creates **2 customer groups (clusters)**.

## 🛠️ Libraries Used

* Python
* Pandas
* Scikit-learn
* Matplotlib

## 📊 Dataset

Sample customer data is created manually:

| Customer | Age | Spending |
| -------- | --: | -------: |
| Riya     |  20 |      100 |
| Aman     |  30 |      200 |
| Faizan   |  40 |      300 |
| Neha     |  22 |      110 |
| Imran    |  38 |      290 |
| Sneh     |  25 |      130 |

## 🔍 How It Works

### 1. Select Features

```python
x = df[["Age", "Spending"]]
```

The model uses Age and Spending to find similarities between customers.

### 2. Create K-Means Model

```python
model = KMeans(n_clusters=2, random_state=42, n_init=10)
```

* `n_clusters=2` → creates 2 groups.
* `random_state=42` → gives reproducible results.
* `n_init=10` → runs K-Means multiple times and selects a better result.

### 3. Assign Customers to Groups

```python
df["Group"] = model.fit_predict(x)
```

`fit_predict()` learns the clusters from the data and assigns each customer a group number such as `0` or `1`.

### 4. Visualize the Groups

Matplotlib is used to display customers from different groups on a scatter plot.

* X-axis → Age
* Y-axis → Spending
* Each group is displayed separately.

## 🎯 Learning Goal

The main purpose of this project is to understand:

* Unsupervised Learning
* K-Means Clustering
* Customer Segmentation
* `fit_predict()`
* Data visualization
* Clustering based on multiple features

## 📈 Example Use Case

K-Means can be used in real-world customer segmentation to identify groups such as:

* Low-spending customers
* High-spending customers
* Younger customers
* Older customers

This can help businesses understand customer behavior and create different strategies for different customer groups.

## 🚀 Conclusion

This project demonstrates how **K-Means clustering** can automatically divide customers into groups based on their Age and Spending without providing predefined labels.
