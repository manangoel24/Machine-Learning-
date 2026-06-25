# 🍕 Linear Regression

## Problem Statement

The objective of this project is to predict the price of a pizza using **Linear Regression**, one of the simplest and most widely used Machine Learning algorithms.

For this project, we use a single feature: **Diameter**.

The goal is to understand whether the size of a pizza alone can help predict its price.

While pizza prices are influenced by many factors, this project focuses on learning the fundamentals of Machine Learning by starting with just one input feature.

---

## Why This Model?

Linear Regression is often the first Machine Learning algorithm people learn because it introduces the core idea of making predictions from data.

It helps us understand how a machine can identify relationships between variables and use those relationships to estimate values it has never seen before.

Since our goal is to predict a numerical value, which is the **pizza price**, Linear Regression is a natural starting point.

---

## How Does It Make Predictions?

Imagine plotting the diameter of every pizza on a graph along with its price.

Some pizzas are small and inexpensive, while others are larger and cost more.

Linear Regression looks at all of these data points and draws the **best-fit straight line** through them. This line represents the relationship between pizza diameter and price.

When we enter the diameter of a new pizza, the model finds where that diameter falls on the line and uses it to estimate the expected price.

The model learns this relationship from the training data rather than memorizing individual pizzas. Once trained, it can make predictions for new pizzas that it has never seen before.

---

## Technical Implementation

* **Programming Language:** Python
* **Libraries:** Pandas, Scikit-learn
* **Machine Learning Model:** Linear Regression
* **Feature Used:** Diameter
* **Target Variable:** Price

---

## Model Workflow

1. Load the pizza dataset.
2. Select **Diameter** as the independent variable.
3. Select **Price** as the dependent variable.
4. Train the Linear Regression model using the dataset.
5. Evaluate the model using the R² score.
6. Accept a pizza diameter as input.
7. Predict the corresponding pizza price.

---

## Model Performance

The model achieved an **R² score of approximately 0.44**.

This means that the pizza's diameter explains about **44% of the variation in its price**.

The remaining variation is caused by factors that are not included in this model, such as toppings, cheese, crust type, brand, and specialty offerings.

Although the accuracy is not very high, this is expected because the model is learning from only a single feature.

The primary objective of this project is to understand how Linear Regression works rather than to build the most accurate price prediction model.

---

## How Is It Different From Multiple Linear Regression?

Linear Regression learns from only **one independent feature**.

In this project, that feature is the pizza's **Diameter**.

In the next project, we'll explore **Multiple Linear Regression**, where the model can learn from several features at the same time, such as diameter, cheese, toppings, crust type, and other characteristics.

By providing more information, the model often produces more accurate predictions than using a single feature alone.
