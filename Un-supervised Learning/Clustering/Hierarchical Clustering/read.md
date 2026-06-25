# 🧩 Hierarchical Clustering

## Overview

Unlike K-Means, Hierarchical Clustering does **not** require us to choose the number of clusters before training.

Instead, it:

1. Starts by treating every data point as its own cluster.
2. Measures the distance between clusters.
3. Merges the two closest clusters.
4. Repeats this process until all data points belong to one large cluster.

The only difference between the different Hierarchical Clustering methods is **how the distance between two clusters is calculated.**

---

# 1. Ward Linkage

Ward Linkage merges the two clusters that result in the **smallest increase in variance**.

Instead of simply looking at the distance between points, it tries to keep each cluster as compact as possible.

From our output, Ward Linkage produced well-balanced customer groups.

For example:

* Cluster 0 → High-spending customers
* Cluster 1 → Low-spending customers
* Cluster 2 → Medium-spending customers

Ward Linkage usually creates the most evenly sized and compact clusters.

It is the most commonly used linkage method.

---

# 2. Single Linkage

Single Linkage measures the distance between the **closest two points** from different clusters.

Suppose:

Cluster A

```text
●     ●
```

Cluster B

```text
      ●     ●
```

Only the shortest distance is considered.

Because of this, clusters can grow like chains.

This is known as the **Chaining Effect**.

In our dataset:

* Most customers were grouped into one very large cluster.
* Only a few extreme customers formed separate clusters.

Single Linkage is useful when long chain-shaped clusters exist but is more sensitive to noise.

---

# 3. Complete Linkage

Complete Linkage measures the distance between the **farthest two points** from different clusters.

Instead of using the nearest points, it waits until every point in both clusters is relatively close.

This produces:

* Smaller clusters
* More compact clusters
* Better separation between groups

Compared to Single Linkage, Complete Linkage avoids the chaining effect.

---

# 4. Average Linkage

Average Linkage calculates the **average distance** between every point in one cluster and every point in another cluster.

Instead of using only:

* the nearest point (Single Linkage), or
* the farthest point (Complete Linkage),

it considers all pairwise distances and takes their average.

This creates clusters that are balanced between Single and Complete Linkage.

Average Linkage is less affected by outliers and usually produces stable clusters.

---

# Comparison of Linkage Methods

| Method           | Distance Used    | Result                                 |
| ---------------- | ---------------- | -------------------------------------- |
| Single Linkage   | Closest points   | Can create long chains                 |
| Complete Linkage | Farthest points  | Compact clusters                       |
| Average Linkage  | Average distance | Balanced clusters                      |
| Ward Linkage     | Minimum variance | Most compact and evenly sized clusters |

---

# Which Linkage Should You Use?

* **Ward Linkage** → When you want compact and balanced clusters (most common)
* **Single Linkage** → When data naturally forms chains
* **Complete Linkage** → When well-separated compact clusters are needed
* **Average Linkage** → When you want a balance between Single and Complete Linkage

---

# K-Means vs Hierarchical Clustering

| K-Means                       | Hierarchical Clustering                               |
| ----------------------------- | ----------------------------------------------------- |
| Must choose K before training | K is not required initially                           |
| Uses centroids                | Uses distances between clusters                       |
| Fast on large datasets        | Slower on large datasets                              |
| Creates clusters directly     | Builds clusters step-by-step                          |
| Best for large datasets       | Best for understanding relationships between clusters |
