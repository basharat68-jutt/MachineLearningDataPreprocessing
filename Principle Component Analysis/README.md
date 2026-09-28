# 📊 Principal Component Analysis (PCA)

A Machine Learning practice project demonstrating **Principal Component Analysis (PCA)** for reducing multiple features into a smaller number of components while preserving important information from the original data.

## 📌 Project Overview

In this project, PCA is applied to a small dataset containing information about:

* Age
* Income
* Spending
* Savings

The data is first standardized using `StandardScaler`, and then PCA is used to reduce the original **4 features into 2 principal components**.

The final two components are visualized using a 2D scatter plot.

## 📊 Dataset

The dataset contains the following features:

| Feature  | Description          |
| -------- | -------------------- |
| Age      | Age of the person    |
| Income   | Income of the person |
| Spending | Spending score       |
| Savings  | Amount of savings    |

Example data:

```text
Age      Income    Spending    Savings
25       30000     70          1000
30       40000     60          5000
35       50000     50          8000
40       60000     40          10000
45       70000     30          15000
50       80000     20          20000
```

## 🔄 Data Standardization

Before applying PCA, the features are standardized using `StandardScaler`.

```python
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
```

Standardization puts the features on a similar scale so that features with larger numerical values do not dominate the PCA transformation.

## 🧩 Applying PCA

PCA is applied with:

```python
pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_data)
```

The original 4 features are reduced to 2 components:

```text
PCA1
PCA2
```

This transforms the dataset from:

```text
4 Features → 2 Principal Components
```

## 📈 Explained Variance

The amount of information captured by each principal component is calculated using:

```python
explained_variance = pca.explained_variance_ratio_
```

The values are converted into percentages:

```python
np.round(explained_variance * 100, 2)
```

This shows how much of the total variance/information is captured by each PCA component.

## 📊 PCA Visualization

A scatter plot is created using `PCA1` and `PCA2`:

```python
plt.scatter(
    pca_df["PCA1"],
    pca_df["PCA2"]
)
```

The visualization provides a **2D representation** of the original 4-dimensional dataset.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

## 📂 Project Structure

```text
PCA/
│
├── PCA.ipynb
└── README.md
```

## 🎯 Learning Outcomes

Through this project, I practiced:

* Understanding PCA
* Dimensionality Reduction
* Feature Standardization
* `StandardScaler`
* `PCA(n_components=2)`
* `fit_transform()`
* Explained Variance
* Creating PCA DataFrames
* Visualizing reduced-dimensional data

## 🚀 Key Concept

PCA is a **dimensionality reduction technique** that transforms the original features into a smaller number of new features called **principal components**.

In this project:

```text
Original Data
4 Features
     ↓
StandardScaler
     ↓
PCA
     ↓
2 Components
     ↓
PCA1 + PCA2
     ↓
2D Visualization
```

---

**Project Type:** Machine Learning — Dimensionality Reduction
**Technique:** Principal Component Analysis (PCA)
**Original Features:** 4
**Reduced Features:** 2
