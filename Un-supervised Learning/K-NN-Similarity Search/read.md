# 🍕 Pizza Similarity Search using K-Nearest Neighbors (KNN)

## Problem Statement

The objective of this project is to find pizzas that are most similar to a selected pizza using the **K-Nearest Neighbors (KNN)** algorithm.

This project comes under **Unsupervised Learning (Similarity Search)**.

Unlike KNN Classification, there is **no target output (y)**. The algorithm simply measures the similarity between pizzas based on their features.

The input features are:

* Company
* Pizza Name
* Type
* Diameter

The output is:

* The K most similar pizzas

---

## Why This Model?

Sometimes we don't want to predict anything.

Instead, we simply want to answer questions like:

* Which pizzas are most similar to this pizza?
* Which products look alike?
* Which movies are similar?
* Which customers behave similarly?

This is called **Similarity Search**.

K-Nearest Neighbors measures the distance between data points and returns the closest ones.

---

## How Does KNN Similarity Search Work?

Suppose we have one selected pizza.

```text
Pizza A
```

The algorithm calculates the distance from Pizza A to every other pizza in the dataset.

For example:

| Pizza   | Distance from Pizza A |
| ------- | --------------------- |
| Pizza B | 1.2                   |
| Pizza C | 0.8                   |
| Pizza D | 2.5                   |
| Pizza E | 1.0                   |
| Pizza F | 3.1                   |

The distances are then sorted.

```text
Pizza C → 0.8
Pizza E → 1.0
Pizza B → 1.2
Pizza D → 2.5
Pizza F → 3.1
```

If **K = 3**, the algorithm returns:

* Pizza C
* Pizza E
* Pizza B

These are the three most similar pizzas.

---

## How Is Similarity Measured?

KNN usually uses **Euclidean Distance**.

For two pizzas:

**Pizza 1**

* Diameter = 10
* Price = 6

**Pizza 2**

* Diameter = 12
* Price = 8

Distance:

```text
√((12−10)² + (8−6)²)

= √(4 + 4)

= √8

≈ 2.83
```

Smaller distance means more similar.

Larger distance means less similar.

---

## Flow of the Algorithm

The KNN Similarity Search follows these steps:

1. Select one pizza.
2. Calculate the distance between this pizza and every other pizza.
3. Sort all distances.
4. Pick the nearest K pizzas.
5. Return those pizzas as the most similar pizzas.

Notice that nothing is being predicted.

The model is only searching for similar data points.

---

## Technical Implementation

Programming Language: Python

Libraries: Pandas, Scikit-learn

Machine Learning Model: K-Nearest Neighbors

Features Used:

Company
Pizza Name
Type
Diameter

Target Variable: None

Since this is an unsupervised learning task, there is no target variable.

---

## Understanding the Output

The first pizza is selected.

For example:

```text
Hand Tossed
Small (10")
Cheeses Pizza
```

The algorithm calculates its distance from every other pizza.

Then it returns the five pizzas with the smallest distances.

These pizzas are considered the most similar because their features are closest to the selected pizza.

---

## Where Is Similarity Search Used?

KNN Similarity Search is commonly used in:

* Product Recommendation
* Movie Recommendation
* Music Recommendation
* Image Search
* Customer Recommendation
* Similar Product Search
* Face Recognition

---

## KNN Similarity Search vs KNN Classification

| KNN Similarity Search (Unsupervised) | KNN Classification (Supervised) |
| ------------------------------------ | ------------------------------- |
| Uses only X                          | Uses X and y                    |
| No target variable                   | Has a target variable           |
| Finds similar data points            | Predicts a class                |
| Returns nearest neighbors            | Returns predicted category      |
| No training labels required          | Training labels are required    |
| Used for recommendation systems      | Used for prediction problems    |

---

## Key Learning

KNN Similarity Search is an **unsupervised learning algorithm** because it does not learn from labels or predict any output.

Instead, it compares feature values, calculates distances, and returns the nearest data points.

It is widely used in recommendation systems and search engines where the goal is to find items that are most similar to a given item.
