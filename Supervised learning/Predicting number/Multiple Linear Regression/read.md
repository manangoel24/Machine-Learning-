# 🍕 Multiple Linear Regression

## Problem Statement

The objective of this project is to predict the price of a pizza using **Multiple Linear Regression**.

Unlike Linear Regression, which predicts the price using only a single feature, Multiple Linear Regression uses multiple features to make a prediction. In this project, the model predicts the pizza price using the company, pizza name, pizza type, and diameter.

The goal is to understand how adding more relevant information helps improve the model's predictions.

---

## Why This Model?

In real-world problems, a single feature is rarely enough to make accurate predictions.

For example, the price of a pizza does not depend only on its diameter. It is also influenced by factors such as the pizza company, the type of pizza, specialty offerings, and other characteristics.

Multiple Linear Regression allows the model to learn from several independent variables at the same time, giving it more information to make better predictions than Linear Regression.

---

## How Does It Make Predictions?

Multiple Linear Regression works similarly to Linear Regression but instead of learning from just one feature, it learns from several features simultaneously.

The model studies how each feature—such as the pizza company, pizza name, pizza type, and diameter—contributes to the final pizza price. During training, it assigns a weight to each feature based on how strongly it influences the price.

When a new pizza is provided, the model combines the contribution of all these features to calculate the predicted price.

By considering multiple characteristics instead of only one, the model is able to capture more information from the dataset, resulting in more accurate predictions.

---

## Technical Implementation

Programming Language: Python

Libraries: Pandas, Scikit-learn

Machine Learning Model: Multiple Linear Regression

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

Train the Multiple Linear Regression model.

Evaluate the model using the R² score.

---

## Why Isn't There a def Function?

In the Linear Regression project, we created a `PizzaPrediction()` function so that users could enter a pizza diameter and receive a predicted price.

For this project, our primary objective is to understand how Multiple Linear Regression learns from multiple features and to evaluate its overall performance.

Since the focus is on comparing the algorithm rather than making individual predictions, a separate prediction function is not included. Once we begin building complete Machine Learning applications, adding prediction functions will become useful again.

---

## Model Performance

The Multiple Linear Regression model achieved an **R² score of approximately 0.987**.

This means the model is able to explain about **98.7% of the variation** in pizza prices, making it significantly more accurate than the earlier Linear Regression model.

The improvement comes from using multiple features instead of relying solely on the pizza's diameter. By learning from additional information such as the company, pizza name, and pizza type, the model gains a much better understanding of the factors that influence pizza prices.

---

## How Is It Different From Linear Regression?

Both Linear Regression and Multiple Linear Regression predict continuous numerical values, such as the price of a pizza.

The main difference is the number of input features they use.

Linear Regression learns from only one independent variable, making it simple but limited when several factors influence the target value.

Multiple Linear Regression learns from several independent variables simultaneously, allowing it to capture more complex relationships within the data. As a result, it generally produces more accurate predictions when multiple features contribute to the outcome.
