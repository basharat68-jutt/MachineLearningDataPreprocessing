# Confusion Matrix

This project demonstrates how to create and visualize a **Confusion Matrix** using Python, Scikit-learn, Matplotlib, and Seaborn.

## What is a Confusion Matrix?

A Confusion Matrix is used to evaluate the performance of a **classification model**.

It compares:

* **Actual Labels** → The real answers
* **Predicted Labels** → The answers predicted by the model

For binary classification, it contains four values:

|              |         Predicted 0 |         Predicted 1 |
| ------------ | ------------------: | ------------------: |
| **Actual 0** |  True Negative (TN) | False Positive (FP) |
| **Actual 1** | False Negative (FN) |  True Positive (TP) |

## Libraries Used

* Python
* Scikit-learn
* Matplotlib
* Seaborn

## How It Works

The `confusion_matrix()` function from Scikit-learn compares the actual values (`y_true`) with the predicted values (`y_pred`).

```python
cm = confusion_matrix(y_true, y_pred)
```

The resulting matrix is visualized using Seaborn's `heatmap()`:

```python
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)
```

### Parameters

* `annot=True` → Displays the values inside the cells.
* `fmt="d"` → Displays values as integers.
* `cmap="Blues"` → Applies the blue color theme.
* `xticklabels` → Shows predicted labels.
* `yticklabels` → Shows actual labels.

## Example Result

For the given data, the confusion matrix is:

```text
[[4 1]
 [1 3]]
```

This means:

* **TN = 4**
* **FP = 1**
* **FN = 1**
* **TP = 3**

This practice helps understand how classification models are evaluated and is an important concept for Machine Learning.
