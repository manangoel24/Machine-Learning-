# 🍕 Decision Tree

## Problem Statement

The objective of this project is to predict **whether a customer will buy a pizza or not** using a **Decision Tree Classifier**.

Like Logistic Regression, KNN, and Naive Bayes, Decision Tree is used for **classification problems**, where the output is a category rather than a numerical value.

In this project, the model predicts whether a customer is likely to buy a pizza using features such as the company, pizza name, pizza type, and diameter.

The output is binary:

* **0 → Customer will not buy the pizza**
* **1 → Customer will buy the pizza**

---

## Why This Model?

Decision Tree is useful because it makes predictions in a way that is easy to understand.

Instead of using probabilities like Naive Bayes or nearest examples like KNN, a Decision Tree makes decisions using a series of rules.

It works like a flowchart. At each step, the model asks a question about the data and moves to the next branch based on the answer.

This makes Decision Trees beginner-friendly because their prediction process is easier to visualize and explain.

---

## How Does It Make Predictions?

A Decision Tree predicts by splitting the data into smaller and smaller groups.

For example, the model may ask questions like:

* Is the pizza from a particular company?
* Is the pizza type vegetarian or non-vegetarian?
* Is the diameter above a certain value?
* Does this pizza name appear more often in the **Bought** category?

Based on these answers, the model moves through the tree until it reaches a final decision.

At the end of the tree, it predicts whether the pizza will be:

* **Bought**
* **Not Bought**

The model learns these rules from the training data. It chooses the splits that best separate the two classes.

---

## Technical Implementation

Programming Language: Python

Libraries: Pandas, Scikit-learn

Machine Learning Model: Decision Tree Classifier

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

Train the Decision Tree Classifier.

Evaluate the model using accuracy.

---

## Model Performance

The Decision Tree Classifier achieved an **accuracy of 100%** on this dataset.

This means the model correctly classified all pizzas in the dataset as either **Bought** or **Not Bought**.

However, a very high accuracy should be interpreted carefully. Since the model is evaluated on the same data it was trained on, it may have memorized the training data instead of learning patterns that generalize well to new data.

This is known as **overfitting**.

So while the accuracy looks perfect, we would need a train-test split or cross-validation later to check whether the model performs well on unseen data.

---

## How Is It Different From Naive Bayes?

Both Naive Bayes and Decision Tree are classification algorithms, but they make predictions differently.

**Naive Bayes** uses probability. It calculates which class is more likely based on the features.

**Decision Tree** uses rules. It asks a sequence of questions and follows branches until it reaches a final prediction.

In simple terms:

* **Naive Bayes asks:** *"Which class is more probable?"*
* **Decision Tree asks:** *"Which rule path does this pizza follow?"*

This makes Decision Tree easier to understand visually because its decision-making process looks like a flowchart.
