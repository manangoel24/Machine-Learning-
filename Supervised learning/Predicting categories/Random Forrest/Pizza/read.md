# 🍕 Random Forest Classification

## Problem Statement

The objective of this project is to predict **whether a customer will buy a pizza or not** using a **Random Forest Classifier**.

Like Logistic Regression, KNN, Naive Bayes, and Decision Tree, Random Forest is used for **classification problems**, where the output is a category rather than a numerical value.

In this project, the model predicts whether a customer is likely to buy a pizza using features such as the company, pizza name, pizza type, and diameter.

The output is binary:

* **0 → Customer will not buy the pizza**
* **1 → Customer will buy the pizza**

---

## Why This Model?

A Decision Tree makes predictions using one tree of rules. While this is easy to understand, one tree can sometimes memorize the training data too closely.

Random Forest improves this by using **many decision trees** instead of just one.

Each tree makes its own prediction, and the final answer is decided by majority vote. This makes Random Forest more stable and reliable than a single Decision Tree.

---

## How Does It Make Predictions?

Random Forest creates multiple decision trees using the training data.

Each tree learns different rules from the dataset. For example, one tree may focus more on pizza diameter, while another tree may focus more on pizza type or company.

When a new pizza is given to the model, every tree gives its own prediction:

* Buy
* Not Buy

The Random Forest then checks which prediction appears most often.

For example:

* Tree 1 → Buy
* Tree 2 → Buy
* Tree 3 → Not Buy
* Tree 4 → Buy
* Tree 5 → Not Buy

Since most trees predicted **Buy**, the final prediction becomes:

**1 → Customer will buy the pizza**

This process is called **majority voting**.

---

## Technical Implementation

Programming Language: Python

Libraries: Pandas, Scikit-learn

Machine Learning Model: Random Forest Classifier

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

Select **Bought** as the target variable.

Train the Random Forest Classifier.

Evaluate the model using accuracy.

---

## Model Performance

The Random Forest Classifier achieved an **accuracy of 100%** on this dataset.

This means the model correctly classified all pizzas in the dataset as either **Bought** or **Not Bought**.

However, since the model is evaluated on the same data it was trained on, this perfect accuracy should be interpreted carefully. The model may have learned the training data very closely.

To check whether the model performs well on unseen data, we can later use a train-test split or cross-validation.

---

## How Is It Different From Decision Tree?

Both Decision Tree and Random Forest make predictions using rule-based decision paths.

The main difference is that **Decision Tree uses only one tree**, while **Random Forest uses many decision trees**.

A single Decision Tree can be easy to understand, but it may overfit the training data.

Random Forest reduces this risk by combining predictions from multiple trees. Instead of depending on one tree's decision, it takes the majority vote from many trees.

In simple terms:

* **Decision Tree asks:** *"What does one tree decide?"*
* **Random Forest asks:** *"What do most trees decide?"*

This makes Random Forest more stable and usually more reliable than a single Decision Tree.
