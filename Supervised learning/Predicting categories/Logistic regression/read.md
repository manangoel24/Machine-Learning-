# 🍕 Logistic Regression

## Problem Statement

The objective of this project is to predict whether a customer will buy a pizza using **Logistic Regression**, one of the most widely used classification algorithms in Machine Learning.

Unlike **Linear Regression**, which predicts a numerical value such as a pizza's price, Logistic Regression predicts a category. In this project, the model determines whether a customer is likely to purchase a pizza based on its **Diameter**.

The output is binary:

* **0** → Customer will not buy the pizza
* **1** → Customer will buy the pizza

---

## Why This Model?

Many real-world problems require us to make decisions rather than predict numbers. For example:

* Will a customer buy a product?
* Is an email spam or not?
* Will a patient have a disease?
* Will a student pass an exam?

These questions have a limited number of possible outcomes, making them **classification problems**.

Logistic Regression is one of the simplest and most effective algorithms for solving binary classification problems. It not only predicts the class but also provides the probability of each outcome, helping us understand how confident the model is in its prediction.

---

## How Does It Make Predictions?

Instead of drawing a straight line like Linear Regression, Logistic Regression learns the relationship between the input feature and the target class using an **S-shaped (Sigmoid) curve**.

For every pizza diameter, the model calculates the probability that a customer will purchase the pizza. This probability always lies between **0 and 1**.

For example:

* **Probability = 0.18** → 18% chance of buying
* **Probability = 0.49** → 49% chance of buying
* **Probability = 0.91** → 91% chance of buying

The model then compares this probability with a threshold (typically **0.5**):

* If the probability is **greater than or equal to 0.5**, it predicts **1 (Buy)**.
* If the probability is **less than 0.5**, it predicts **0 (Do Not Buy)**.

This allows the model to make classification decisions while also indicating how confident it is about each prediction.

---

## Technical Implementation

* **Programming Language:** Python
* **Libraries:** Pandas, Scikit-learn
* **Machine Learning Model:** Logistic Regression
* **Feature Used:** Diameter
* **Target Variable:** Bought

---

## Model Workflow

1. Load the pizza dataset.
2. Select **Diameter** as the independent variable.
3. Select **Bought** as the dependent variable.
4. Train the Logistic Regression model.
5. Evaluate the model using classification accuracy.
6. Accept a pizza diameter as input.
7. Predict whether the customer will buy the pizza.
8. Display the probability of buying the pizza.

---

## Model Performance

The model achieved an **accuracy of approximately 56.25%**.

Accuracy represents the percentage of predictions the model classified correctly.

Although the model performs better than random guessing, the accuracy is relatively modest because it is learning from only a single feature—the pizza's diameter.

In reality, a customer's buying decision depends on many additional factors such as price, toppings, cheese, personal preference, promotions, and brand.

The objective of this project is to understand how Logistic Regression performs binary classification rather than to build a highly accurate purchase prediction system.

---

## How Is It Different From Linear Regression?

Although both algorithms belong to **Supervised Learning**, they solve different types of problems.

**Linear Regression** predicts a **continuous numerical value**, such as the price of a pizza.

**Logistic Regression** predicts a **category**, such as whether a customer will buy a pizza or not.

Another important difference is that Logistic Regression also provides the **probability** of each prediction. Instead of simply saying **"Buy"** or **"Don't Buy,"** it tells us how likely that outcome is, making it especially useful for decision-making problems.
