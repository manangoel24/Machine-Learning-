# 🍕 Lasso Regression

## How Does It Make Predictions?

Lasso Regression learns from all the available input features, such as the pizza company, pizza name, pizza type, and diameter, to estimate the price of a pizza.

During training, the model determines how much each feature contributes to the final prediction. Features that have a strong influence are assigned higher importance, while features that contribute very little are gradually reduced.

If a feature provides almost no useful information, Lasso Regression can completely eliminate it by assigning its weight to zero. The final prediction is then made using only the remaining important features.

This allows the model to focus on the most relevant information while ignoring unnecessary features.

---

## Technical Implementation

Programming Language: Python

Libraries: Pandas, Scikit-learn

Machine Learning Model: Lasso Regression

Features Used:

Company
Pizza Name
Type
Diameter

Target Variable: Price

---

## Model Workflow

Load the pizza dataset.

Select the input features (Company, Pizza Name, Type, and Diameter).

Convert the categorical features into numerical values using one-hot encoding (`get_dummies()`).

Select Price as the target variable.

Train the Lasso Regression model.

Evaluate the model using the R² score.

---

## Model Performance

The Lasso Regression model achieved an **R² score of approximately 0.427**.

This score is considerably lower than the scores obtained by Multiple Linear Regression and Ridge Regression. This happens because Lasso Regression applies a stronger penalty to feature weights and may completely remove some features from the model.

While this can reduce prediction accuracy for this particular dataset, it helps create a simpler model by automatically selecting only the most important features. On datasets with many irrelevant or redundant features, Lasso Regression can often perform better and produce models that are easier to interpret.

---

## How Is It Different From Ridge Regression?

Both Ridge Regression and Lasso Regression use regularization to reduce overfitting and improve the model's ability to generalize.

The key difference lies in how they handle feature importance.

Ridge Regression reduces the importance of every feature but keeps all of them in the model.

Lasso Regression can completely remove features by reducing their weights to zero. This means it performs automatic feature selection, allowing the model to identify which features are truly important while ignoring those that contribute very little to the prediction.

Because of this, Lasso Regression is often preferred when working with datasets that contain many unnecessary or redundant features.
