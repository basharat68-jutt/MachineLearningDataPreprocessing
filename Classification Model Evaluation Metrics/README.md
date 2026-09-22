# Classification Model Evaluation Metrics

This project demonstrates how to evaluate a classification machine learning model using four important evaluation metrics:

* Accuracy
* Precision
* Recall
* F1 Score

These metrics are available in `sklearn.metrics`.

## Libraries Used

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
```

## Dataset

### Actual Answers (`y_true`)

```python
y_true = [1,0,1,1,0,1,0]
```

`y_true` contains the actual answers — yani reality mein kya hua.

### Model Predictions (`y_pred`)

```python
y_pred = [1,0,1,0,0,1,1]
```

`y_pred` contains the answers predicted by the machine learning model.

## 1. Accuracy

```python
accuracy_score(y_true, y_pred)
```

Accuracy batati hai ke model ne **total predictions mein se kitni predictions correctly predict ki hain**.

### Formula

```text
Accuracy = Correct Predictions / Total Predictions
```

Example:

Agar model ne 100 predictions ki aur 95 correct hain:

```text
Accuracy = 95 / 100 = 0.95 = 95%
```

**Simple meaning:**

> Total predictions mein se model ne kitni predictions sahi ki?

---

## 2. Pr
