## Understanding the Cluster Results

After training the K-Means model, each pizza was assigned to one of the four clusters.

To understand what each cluster represents, we calculated the **average diameter** of the pizzas inside each cluster.

```python
print(df.groupby("Cluster")["Diameter"].mean())
```

The output was:

| Cluster | Average Diameter |
| ------: | ---------------: |
|       0 |        12 inches |
|       1 |        16 inches |
|       2 |        10 inches |
|       3 |        14 inches |

From this, we can interpret the clusters as:

* **Cluster 2** → Small pizzas (10")
* **Cluster 0** → Medium pizzas (12")
* **Cluster 3** → Large pizzas (14")
* **Cluster 1** → Extra Large pizzas (16")

Notice that the model was **never told** which pizzas were Small, Medium, Large, or Extra Large.

It only looked at the pizza data and grouped similar pizzas together based on their features.

After clustering, we interpreted each cluster by calculating its average diameter.

---

## Choosing the Number of Clusters (K)

One important decision in K-Means is selecting the value of **K**, which represents the number of clusters.

To find a suitable value, we used the **Elbow Method**.

The model was trained multiple times using different values of K:

* K = 1
* K = 2
* K = 3
* K = 4
* ...
* K = 10

For every value of K, the model calculated **Inertia**.

Inertia measures how close the pizzas are to the center of their assigned cluster.

Lower inertia means the pizzas inside a cluster are more similar.

Our results were:

|  K | Inertia |
| -: | ------: |
|  1 |  780.73 |
|  2 |  315.15 |
|  3 |  262.44 |
|  4 |  203.06 |
|  5 |  191.95 |
|  6 |  180.75 |
|  7 |  168.09 |
|  8 |  151.82 |
|  9 |  146.81 |
| 10 |  135.62 |

We can observe that:

* The inertia decreases sharply from **K = 1** to **K = 4**.
* After **K = 4**, the decrease becomes much smaller.
* Adding more clusters after this point does not provide a significant improvement.

Therefore, we selected:

**K = 4**

because it provides a good balance between:

* Meaningful pizza groups
* Lower inertia
* Simpler model

This point is known as the **Elbow Point**, where adding additional clusters gives only marginal improvement.
