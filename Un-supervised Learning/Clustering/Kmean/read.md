# 🧩 Customer Segmentation using K-Means Clustering

## Problem Statement

The objective of this project is to group customers into different segments using **K-Means Clustering**.

This project comes under **Unsupervised Learning**, where the model only has input data (**X**) and no target output (**y**).

Unlike supervised learning models, K-Means does not predict a price or category. Instead, it finds hidden patterns in the data and groups similar customers together.

The input features are:

* Spending
* Visits
* Average Bill
* Items Bought

The output is:

* Cluster number assigned to each customer

---

## Why This Model?

K-Means is one of the most common clustering algorithms used in Machine Learning.

It is useful when we want to understand customer behavior without already having labels.

For example, a business may not know what types of customers it has. K-Means can help group customers into segments such as:

* High spending customers
* Low spending customers
* Frequent visitors
* Occasional buyers
* Customers with high average bills

This helps businesses understand their customers better and make better decisions.

---

## How Does It Make Groups?

K-Means starts by creating a fixed number of clusters.

In this project, we created **4 clusters**.

The model then tries to place customers into groups based on similarity.

Customers with similar spending, visits, average bill, and items bought are placed in the same cluster.

The model works by finding the center point of each cluster, called a **centroid**.

Then it follows this process:

1. Randomly create cluster centers.
2. Assign each customer to the nearest cluster center.
3. Recalculate the center of each cluster.
4. Repeat the process until the clusters become stable.

Once the model finishes, each customer gets assigned a cluster number.

---

## Technical Implementation

Programming Language: Python

Libraries: Pandas, Scikit-learn

Machine Learning Model: K-Means Clustering

Features Used:

Spending
Visits
Average Bill
Items Bought

Target Variable: None

Since this is unsupervised learning, there is no target variable.

---

## Model Workflow

Load the customer dataset.

Select the input features.

Create the K-Means model.

Set the number of clusters to **4**.

Train the model using customer data.

Assign each customer to a cluster.

Add the cluster result back to the dataset.

Calculate the average values of each cluster.

Use the Elbow Method to understand how many clusters may be suitable.

---

## Cluster Interpretation

After clustering, the model groups customers based on similar behavior.

The average values of each cluster help us understand what each group represents.

For example:

* One cluster may contain customers with high spending and high items bought.
* Another cluster may contain customers with low spending and fewer visits.
* Another cluster may contain customers who visit often but spend less.
* Another cluster may contain customers with high average bill values.

This helps us convert raw customer data into meaningful customer segments.

---

## Elbow Method

The Elbow Method is used to understand how many clusters may be suitable for the dataset.

The model is trained with different cluster values such as **1, 2, 3, 4**, and so on.

For each value of **K**, the model calculates **Inertia**.

Inertia tells us how tightly the customers are grouped inside each cluster.

As the number of clusters increases, inertia usually decreases. However, after a certain point, the improvement becomes much smaller.

That point is called the **Elbow Point**.

The Elbow Point helps us choose a reasonable number of clusters.

---

## Choosing the Value of K (Number of Clusters)

One important decision in K-Means is choosing the value of **K**, which represents the number of clusters.

In this project, we used the **Elbow Method** to determine the most suitable value of K.

The model was trained multiple times using different values of K:

```text
K = 1
K = 2
K = 3
K = 4
...
K = 10
```

For each value of K, the model calculated **Inertia**.

Inertia measures how close the data points are to their assigned cluster center.

Lower inertia means customers inside a cluster are more similar.

As K increases, inertia always decreases because more clusters can fit the data better.

However, after a certain point, the decrease in inertia becomes much smaller. This point is called the **Elbow Point**.

In our results, the inertia decreased significantly from:

```text
K = 1 → K = 2
K = 2 → K = 3
K = 3 → K = 4
```

After **K = 4**, the improvement became much smaller. Adding more clusters did not provide a significant reduction in inertia.

Therefore, we selected:

```text
K = 4
```

because it provides a good balance between:

* Creating meaningful customer groups
* Avoiding unnecessary extra clusters
* Keeping the model simple and easy to interpret

In simple words, **4 clusters were enough to capture the major patterns in the customer data**, while adding more clusters offered very little additional benefit.

---

## How Is It Different From Supervised Learning?

In supervised learning, the model learns from both input and output.

For example:

* Input: Pizza diameter
* Output: Pizza price

or

* Input: Pizza details
* Output: Bought or Not Bought

But in unsupervised learning, there is no output column.

The model only receives the input data and tries to find patterns on its own.

In this project, K-Means does not know customer types in advance. It creates the groups by studying similarities between customers.

---

## Key Learning

K-Means helps us discover hidden groups in data.

It does not predict an output. Instead, it organizes similar records together.

This makes it useful for customer segmentation, market research, product grouping, recommendation systems, and behavior analysis.
