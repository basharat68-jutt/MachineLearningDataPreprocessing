# MAE, MSE & RMSE

This project demonstrates three common **Regression Evaluation Metrics** in Machine Learning:

* **MAE (Mean Absolute Error)**
* **MSE (Mean Squared Error)**
* **RMSE (Root Mean Squared Error)**

## 📌 What are these metrics?

### 1. MAE — Mean Absolute Error

MAE tells us the **average amount by which the model's predictions are wrong**.

Steps:

1. Find the difference between actual and predicted values.
2. Remove the negative sign using absolute value.
3. Add all the errors.
4. Divide by the total number of predictions.

**Use MAE when:**
You want a simple understanding of how much your model is wrong on average.

---

### 2. MSE — Mean Squared Error

MSE squares every error before calculating the average.

Steps:

1. Find the difference between actual and predicted values.
2. Square each error.
3. Add all squared errors.
4. Divide by the total number of predictions.

Because errors are squared, **large mistakes get much more importance**.

**Use MSE when:**
You want large prediction errors to be penalized strongly.

---

### 3. RMSE — Root Mean Squared Error

RMSE is the **square root of MSE**.

It is useful because the error is represented in the **same units as the original data**.

For example, if the model predicts student marks, RMSE is also expressed in marks.

**Use RMSE when:**
You want to understand the model's error in the original units.

---

## 🧪 Example

Actual scores:

```text
90, 60, 80, 100
```

Predicted scores:

```text
85, 70, 70, 95
```

The program calculates:

```text
MAE  → Average absolute error
MSE  → Squared error value
RMSE → Error in the original units
```

## 🛠️ Libraries Used

* Python
* NumPy
* Scikit-learn

## 📚 Concepts Practiced

* Mean Absolute Error
* Mean Squared Error
* Root Mean Squared Error
* Regression Model Evaluation
* `sklearn.metrics`
* NumPy square root
