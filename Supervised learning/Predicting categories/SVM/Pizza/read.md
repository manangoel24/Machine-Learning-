# 🍕 Support Vector Machine (SVM)

## Problem Statement

The objective of this project is to predict **whether a customer will buy a pizza or not** using a **Support Vector Machine (SVM)** classifier.

Like Logistic Regression, KNN, Naive Bayes, Decision Tree, and Random Forest, SVM is used for **classification problems**, where the output is a category rather than a numerical value.

In this project, the model predicts whether a customer is likely to buy a pizza using the pizza's diameter.

The output is binary:

* **0 → Customer will not buy the pizza**
* **1 → Customer will buy the pizza**

---

## Why This Model?

SVM is useful when we want to separate data into different categories using the best possible boundary.

For this project, the model tries to separate pizzas into two groups:

* Pizzas customers are likely to buy
* Pizzas customers are not likely to buy

SVM focuses on finding a boundary that separates these two groups as clearly as possible.

---

## How Does It Make Predictions?

SVM tries to create the best separating boundary between the two classes.

In simple terms, it looks at the data and asks:

> **"Where should I draw the line so that Bought and Not Bought pizzas are separated as clearly as possible?"**

The points closest to this boundary are called **support vectors**. These are important because they help decide where the boundary should be placed.

When a new pizza diameter is given, the model checks which side of the boundary it falls on.

* If it falls on the **Bought** side, the model predicts that the customer will buy the pizza.
* If it falls on the **Not Bought** side, the model predicts that the customer will not buy the pizza.

In this project, we also enabled probability output, so the model can show the probability of the customer buying the pizza.

---

## Technical Implementation

Programming Language: Python

Libraries: Pandas, Scikit-learn

Machine Learning Model: Support Vector Classifier (SVC)

Feature Used:

Diameter

Target Variable: Bought

---

## Model Workflow

Load the pizza dataset.

Select **Diameter** as the input feature.

Select **Bought** as the target variable.

Train the SVM classifier.

Accept a pizza diameter as input.

Predict whether the customer will buy the pizza.

Display the buying probability.

---

## Why Is There a `def` Function?

In this project, a **PizzaPrediction()** function is used to predict whether a customer will buy a pizza for a custom diameter.

A second function, **PizzaProbability()**, is used to display the probability of buying.

This makes the project interactive because we can enter a pizza diameter and directly see both the predicted class and the buying probability.

---

## Example Prediction

**Example Input:**

```text
Diameter = 14
```

**Output:**

```text
Customer will buy the pizza
Buying Probability: 0.5163
```

This means the model predicts that the customer will buy the pizza, with a buying probability of approximately **51.63%**.

---

## How Is It Different From Random Forest?

Both Random Forest and SVM are classification algorithms, but they make predictions differently.

Random Forest uses many decision trees and combines their predictions through majority voting.

SVM tries to find the best boundary that separates the two classes.

In simple terms:

* **Random Forest asks:** *"What do most trees predict?"*
* **SVM asks:** *"Which side of the best boundary does this pizza fall on?"*

Random Forest is rule-based and uses many trees, while SVM is boundary-based and focuses on separating classes as clearly as possible.
