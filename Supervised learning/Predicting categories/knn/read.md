# 🍕 K-Nearest Neighbors (KNN) Classification

## Problem Statement

The objective of this project is to predict whether a customer will buy a pizza or not using **K-Nearest Neighbors (KNN) Classification**.

Like Logistic Regression, KNN Classification is used for classification problems, where the output is a category rather than a numerical value.

In this project, the model predicts whether a customer will buy a pizza using features such as the company, pizza name, pizza type, and diameter.

The output is binary:

* **0** → Customer will not buy the pizza
* **1** → Customer will buy the pizza

---

## Why This Model?

Logistic Regression predicts the buying decision by learning a mathematical relationship between the input features and the target category.

KNN takes a different approach.

Instead of learning a fixed equation, KNN makes predictions by comparing a new pizza with pizzas that already exist in the dataset. It checks which pizzas are most similar and uses them to decide the final category.

This makes KNN easy to understand because it follows a simple idea:

> **Similar pizzas should have similar buying outcomes.**

---

## How Does It Make Predictions?

KNN stands for **K-Nearest Neighbors**.

When a new pizza is given to the model, KNN looks for the **K** most similar pizzas in the dataset. In this project, we use **K = 3**, which means the model checks the **3 nearest pizzas**.

Each of these neighboring pizzas already has a known result: either **Bought** or **Not Bought**.

The model then looks at the majority class among those neighbors.

For example:

* Neighbor 1 → Bought
* Neighbor 2 → Bought
* Neighbor 3 → Not Bought

Since **2 out of 3** neighbors were bought, the model predicts:

**1 → Customer will buy the pizza**

KNN does not create a formula during training. Instead, it stores the data and makes decisions based on similarity when a prediction is needed.

---

## Technical Implementation

Programming Language: Python

Libraries: Pandas, Scikit-learn

Machine Learning Model: K-Nearest Neighbors Classifier

Features Used:

Company
Pizza Name
Type
Diameter

Target Variable: Bought

---

## Model Workflow

Load the pizza dataset.

Select the input features (Company, Pizza Name, Type, and Diameter).

Convert categorical features into numerical values using one-hot encoding (`get_dummies()`).

Select Bought as the target variable.

Train the KNN Classification model.

Set the number of neighbors as **3**.

Evaluate the model using accuracy.

---

## Model Performance

The KNN Classification model achieved an **accuracy of approximately 71.43%**.

This means the model correctly classified around **71.43%** of the pizzas as either **Bought** or **Not Bought**.

This accuracy is higher than the Logistic Regression model in this dataset, suggesting that similarity-based prediction worked better than a simple mathematical classification boundary for this problem.

---

## How Is It Different From Logistic Regression?

Both Logistic Regression and KNN Classification are used for classification problems.

Logistic Regression learns a mathematical relationship between the input features and the target class. It estimates the probability of a pizza being bought and then classifies it as **Bought** or **Not Bought**.

KNN Classification does not learn a fixed equation. Instead, it compares a new pizza with existing pizzas and looks at the closest examples to make a decision.

In simple terms:

* **Logistic Regression** learns a pattern.
* **KNN** looks for similar examples.

This makes KNN more flexible in some cases, especially when the data does not follow a simple linear pattern.
