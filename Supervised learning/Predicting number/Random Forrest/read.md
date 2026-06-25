# 🍕 Random Forest Regression

## Problem Statement

The objective of this project is to predict the price of a pizza using **Random Forest Regression**.

Like the previous regression models, Random Forest Regression predicts a continuous numerical value. In this project, the model predicts the price of a pizza using multiple features such as the company, pizza name, pizza type, and diameter.

The goal is to understand how combining multiple decision trees can help create a more powerful and stable prediction model.

---

## Why This Model?

Linear Regression, Multiple Linear Regression, Ridge Regression, and Lasso Regression are based on relationships between features and the target value. They work well when the pattern in the data is relatively simple.

However, real-world data is often more complex. The price of a pizza may not always increase in a perfectly straight or simple pattern. Different companies, pizza types, and specialty pizzas can affect price in different ways.

Random Forest Regression is useful because it can capture more complex patterns in the data. Instead of relying on one model, it builds multiple decision trees and combines their predictions to produce a final result.

---

## How Does It Make Predictions?

Random Forest Regression works by creating many decision trees.

Each decision tree looks at the data and learns a set of rules to predict the pizza price. For example, one tree may focus more on pizza diameter, while another may focus more on pizza type or company.

When a new pizza is given to the model, every tree makes its own price prediction. The Random Forest model then takes the average of all those predictions to produce the final predicted price.

This makes the model more stable than a single decision tree because it does not depend on only one set of rules. By combining many trees, Random Forest reduces the chance of overfitting and usually gives more reliable predictions.

---

## Technical Implementation

Programming Language: Python

Libraries: Pandas, Scikit-learn

Machine Learning Model: Random Forest Regression

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

Train the Random Forest Regression model.

Evaluate the model using the R² score.

---

## Model Performance

The Random Forest Regression model achieved an **R² score of approximately 0.977**.

This means the model is able to explain about **97.7% of the variation** in pizza prices.

The score is very strong because Random Forest can learn more complex patterns than simple linear models. It does not depend on one straight-line relationship. Instead, it uses many decision trees to understand different rules within the data.

---

## How Is It Different From Lasso Regression?

Both Lasso Regression and Random Forest Regression can use multiple features to predict pizza prices, but they learn from the data in very different ways.

Lasso Regression is still a linear model. It tries to predict the pizza price by assigning weights to features and can remove less important features by reducing their weights to zero.

Random Forest Regression does not depend on a straight-line relationship. Instead, it builds many decision trees, each learning different rules from the data, and then combines their predictions.

This allows Random Forest Regression to capture more complex patterns, making it more flexible than Lasso Regression.
