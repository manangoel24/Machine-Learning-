# 🍕 Naive Bayes

## Problem Statement

The objective of this project is to predict whether a customer will buy a pizza or not using **Naive Bayes**, a probability-based classification algorithm.

Like Logistic Regression and K-Nearest Neighbors (KNN), Naive Bayes is used for classification problems, where the output is a category instead of a numerical value.

In this project, the model predicts whether a customer is likely to buy a pizza using features such as the company, pizza name, pizza type, and diameter.

The output is binary:

* **0** → Customer will not buy the pizza
* **1** → Customer will buy the pizza

---

## Why This Model?

Many classification problems involve uncertainty. Instead of finding similar examples like KNN or learning a mathematical boundary like Logistic Regression, Naive Bayes predicts the outcome by calculating probabilities.

It estimates how likely a pizza belongs to each class based on the information it has learned from the training data and then selects the class with the highest probability.

Because of its simplicity and speed, Naive Bayes is widely used in applications such as spam email detection, sentiment analysis, document classification, and recommendation systems.

---

## How Does It Make Predictions?

Naive Bayes learns the probability of each feature belonging to each class during training.

When a new pizza is provided, the model calculates:

* The probability that the pizza will be **Bought**
* The probability that the pizza will **Not Be Bought**

It then compares these probabilities and predicts the class with the higher probability.

The word **"Naive"** comes from the assumption that every feature is independent of the others. For example, the model assumes that the pizza company, pizza type, and diameter influence the buying decision independently, even though this may not always be true in real life.

Despite this simple assumption, Naive Bayes often performs surprisingly well on many classification problems.

---

## Technical Implementation

Programming Language: Python

Libraries: Pandas, Scikit-learn

Machine Learning Model: Gaussian Naive Bayes

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

Convert the categorical features into numerical values using one-hot encoding (`get_dummies()`).

Select Bought as the target variable.

Train the Gaussian Naive Bayes model.

Evaluate the model using accuracy.

---

## Model Performance

The Naive Bayes model achieved an **accuracy of approximately 86.61%**.

This means the model correctly classified about **86.6%** of the pizzas as either **Bought** or **Not Bought**.

For this dataset, Naive Bayes performed better than both Logistic Regression and KNN Classification. Although it makes a simple assumption that all features are independent, it was still able to classify most pizzas correctly.

---

## How Is It Different From KNN Classification?

Both Naive Bayes and KNN are classification algorithms, but they make predictions in completely different ways.

KNN Classification predicts the class by finding the most similar pizzas in the dataset and using the majority vote of the nearest neighbors.

Naive Bayes does not compare a pizza with other pizzas. Instead, it calculates the probability of each class using the information learned during training and predicts the class with the highest probability.

In simple terms:

* **KNN** asks: *"Which pizzas look most similar to this one?"*
* **Naive Bayes** asks: *"Based on probability, which class is more likely?"*

This probability-based approach makes Naive Bayes extremely fast and efficient, especially when working with large datasets.
