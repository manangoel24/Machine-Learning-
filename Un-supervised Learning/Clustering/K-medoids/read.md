# 🍕 Pizza Clustering using K-Medoids

## Problem Statement

The objective of this project is to group similar pizzas together using **K-Medoids Clustering**.

This project comes under **Unsupervised Learning**, where the model only has input data (**X**) and no target output (**y**).

Unlike supervised learning models, K-Medoids does not predict price or purchase decisions. Instead, it finds hidden groups in the pizza dataset based on similarity.

The input features are:

* Company
* Pizza Name
* Type
* Diameter

The output is:

* Cluster number assigned to each pizza

---

## Why This Model?

K-Medoids is similar to K-Means, but it handles outliers better.

In K-Means, the center of a cluster is calculated using the **average** of all points in that cluster. This center is called a **centroid**.

The problem is that averages can be strongly affected by outliers.

K-Medoids solves this by choosing an actual data point as the center of each cluster. This actual representative point is called a **medoid**.

Because of this, K-Medoids is more stable when the dataset contains extreme values.

---

## Understanding Outliers

An outlier is a value that is very different from the rest of the data.

### Example: Customer Spending

| Customer | Spending |
| -------- | -------: |
| A        |   ₹1,000 |
| B        |   ₹1,200 |
| C        |   ₹1,300 |
| D        |   ₹1,100 |
| E        |  ₹50,000 |

Here, **₹50,000** is an outlier because all the other customers spend around **₹1,000–₹1,300**.

---

## Why Are Outliers a Problem?

### Without the Outlier

Values:

```text
1000
1200
1300
1100
```

Average (Mean):

```text
(1000 + 1200 + 1300 + 1100) / 4 = 1150
```

This average represents the data well.

### With the Outlier

Values:

```text
1000
1200
1300
1100
50000
```

Average (Mean):

```text
(1000 + 1200 + 1300 + 1100 + 50000) / 5 = 10920
```

Now the average becomes **₹10,920**, which does not represent the typical customer at all.

---

## Effect on K-Means

Suppose the customer spending values are:

```text
1000
1200
1300
1100
50000
```

K-Means calculates the **centroid (average)**, so the outlier pulls the cluster center toward **₹50,000**.

Result:

```text
Centroid = 10920
```

This center is far away from where most customers actually are.

---

## Effect on K-Medoids

K-Medoids does **not** calculate an average.

Instead, it chooses **one of the actual data points** as the center of the cluster.

Using the same data:

```text
1000
1200
1300
1100
50000
```

The best representative is likely to be:

```text
1200
```

or

```text
1100
```

The **₹50,000** value has very little influence because the model chooses an existing data point instead of calculating an average.

This makes K-Medoids much more robust when outliers are present.

---

## Technical Implementation

Programming Language: Python

Libraries: Pandas, Scikit-learn-extra

Machine Learning Model: K-Medoids Clustering

Features Used:

Company
Pizza Name
Type
Diameter

Target Variable: None

Since this is an unsupervised learning algorithm, there is no target variable.

---

## Model Workflow

Load the pizza dataset.

Select the input features.

Convert categorical features into numerical values using one-hot encoding (`get_dummies()`).

Create the K-Medoids model.

Set the number of clusters.

Train the model using the pizza dataset.

Assign each pizza to a cluster.

Analyze the clusters using the cluster labels.

---

## Model Interpretation

After training, every pizza is assigned to one of the clusters.

Unlike K-Means, each cluster is represented by an **actual pizza** from the dataset rather than an average point.

This representative pizza is called the **medoid**.

Because the cluster center is always a real data point, K-Medoids is less affected by unusual pizzas or extreme values.

---

## How Is It Different From K-Means?

Both K-Means and K-Medoids are clustering algorithms.

Both are used to group similar data points together.

The main difference is how they choose the center of each cluster.

| K-Means                       | K-Medoids                      |
| ----------------------------- | ------------------------------ |
| Uses a centroid               | Uses a medoid                  |
| Centroid is the average       | Medoid is an actual data point |
| Sensitive to outliers         | More robust to outliers        |
| Faster                        | Slower                         |
| Works well for large datasets | Better when outliers exist     |

In simple terms:

* **K-Means asks:** *"What is the average center of this group?"*
* **K-Medoids asks:** *"Which actual data point best represents this group?"*

Because of this, K-Medoids is often preferred when the dataset contains outliers or extreme values.
