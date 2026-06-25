# 🍕 Ridge Regression

## Problem Statement

The objective of this project is to predict the price of a pizza using Ridge Regression, an improved version of Linear Regression that helps reduce overfitting.

Just like Linear Regression and Multiple Linear Regression, Ridge Regression predicts a continuous numerical value. In this project, the model predicts the price of a pizza using multiple features such as the company, pizza name, type, and diameter.

The goal is to understand how Ridge Regression improves prediction by preventing the model from relying too heavily on any single feature.

---

## Why This Model?

As we add more features to our dataset, the model becomes more powerful, but it also becomes more likely to overfit. Overfitting occurs when a model learns the training data too well, including its noise, resulting in poorer performance on new, unseen data.

Ridge Regression addresses this problem by adding a small penalty to the model during training. This discourages the model from assigning excessively large importance to any single feature, making the predictions more stable and improving the model's ability to generalize.

---

## How Does It Make Predictions?

Ridge Regression works very similarly to Multiple Linear Regression.

It considers all the input features, such as the pizza company, pizza name, pizza type, and diameter, and learns how each feature contributes to the final pizza price.

However, unlike Multiple Linear Regression, Ridge Regression prevents the model from giving extremely high importance (weights) to individual features. Instead, it slightly reduces these weights, resulting in a model that is less sensitive to small variations in the training data.

This process helps the model make more reliable predictions, especially when several features are correlated with one another.

---

## Technical Implementation

Programming Language: Python

Libraries: Pandas, Scikit-learn

Machine Learning Model: Ridge Regression

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

Convert categorical features into numerical values using one-hot encoding (get_dummies()).

Select Price as the target variable.

Train the Ridge Regression model.

Evaluate the model using the R² score.

---

## Why Isn't There a def Function?

In the previous projects, we created a function such as PizzaPrediction() so that we could enter a pizza diameter and receive a prediction.

For this project, the objective is different.

Here, we are only learning how Ridge Regression is trained and how well it performs. Since our focus is on understanding the algorithm rather than making user predictions, a separate prediction function is not required.

Once we begin comparing different models or building complete applications, adding a prediction function will become useful again.

---

## Model Performance

The Ridge Regression model achieved an R² score of approximately 0.925.

This means the model is able to explain about 92.5% of the variation in pizza prices, which is a significant improvement over using only a single feature.

The higher R² score is mainly because the model learns from multiple features rather than relying solely on the pizza's diameter. It also benefits from Ridge Regression's regularization, which helps produce more stable and reliable predictions.

---

## How Is It Different From Multiple Linear Regression?

Both algorithms use multiple input features to predict the price of a pizza.

The key difference is that Multiple Linear Regression allows the model to assign any weight it wants to each feature, even if some weights become excessively large.

Ridge Regression introduces a regularization penalty that keeps these weights under control. Instead of allowing one feature to dominate the prediction, Ridge Regression slightly reduces all feature weights, making the model less likely to overfit and generally more reliable on unseen data.

As datasets become larger and more complex, Ridge Regression often produces more stable predictions.
