# 📊 Pearson Correlation

## What is Pearson Correlation?

Pearson Correlation measures **how strongly two variables are linearly related**.

It tells us whether two variables increase together, decrease together, or have no relationship at all.

Its value always lies between **-1 and +1**.

```text
-1  ←──────── 0 ────────→ +1

-1 → Perfect Negative Correlation

 0 → No Correlation

+1 → Perfect Positive Correlation
```

---

## Example 1: Positive Correlation

Suppose we have the following pizza data:

| Pizza Diameter (inches) | Price ($) |
| ----------------------- | --------- |
| 8                       | 5         |
| 10                      | 7         |
| 12                      | 9         |
| 14                      | 11        |
| 16                      | 13        |

As the diameter increases, the price also increases.

```text
Diameter ↑

Price    ↑
```

Pearson Correlation:

```text
r ≈ +1
```

This means there is a **strong positive relationship** between Diameter and Price.

---

## Example 2: Negative Correlation

Suppose we measure:

| Study Hours | TV Hours |
| ----------- | -------- |
| 2           | 8        |
| 4           | 6        |
| 6           | 4        |
| 8           | 2        |
| 10          | 1        |

As study hours increase, TV hours decrease.

```text
Study Hours ↑

TV Hours    ↓
```

Pearson Correlation:

```text
r ≈ -1
```

This is called a **strong negative correlation**.

---

## Example 3: No Correlation

Suppose we record:

| Shoe Size | Exam Marks |
| --------- | ---------- |
| 6         | 72         |
| 7         | 90         |
| 8         | 65         |
| 9         | 80         |
| 10        | 74         |

Shoe size has nothing to do with exam marks.

```text
Shoe Size ↕

Marks     ↕
```

No consistent pattern exists.

Pearson Correlation:

```text
r ≈ 0
```

This means there is **no linear relationship**.

---

## Interpretation of Pearson Correlation

| Correlation (r) | Meaning                       |
| --------------- | ----------------------------- |
| +1              | Perfect Positive Correlation  |
| +0.8            | Strong Positive Correlation   |
| +0.5            | Moderate Positive Correlation |
| 0               | No Correlation                |
| -0.5            | Moderate Negative Correlation |
| -0.8            | Strong Negative Correlation   |
| -1              | Perfect Negative Correlation  |

---

## How Do We Interpret It?

### Positive Correlation

Both variables move in the same direction.

```text
Diameter ↑

Price    ↑
```

or

```text
Diameter ↓

Price    ↓
```

---

### Negative Correlation

The variables move in opposite directions.

```text
Study Hours ↑

TV Hours    ↓
```

---

### No Correlation

One variable changes independently of the other.

```text
Shoe Size

Exam Marks

(No clear relationship)
```

---

## Why Do We Use Pearson Correlation?

Pearson Correlation helps us understand **which features are useful for predicting another variable**.

If two variables have a strong correlation, one can often help predict the other.

For example:

| Feature       | Correlation with Price |
| ------------- | ---------------------- |
| Diameter      | 0.92                   |
| Cheese Amount | 0.81                   |
| Pizza Color   | 0.05                   |

From this, we can conclude:

* Diameter is strongly related to Price.
* Cheese Amount is also related to Price.
* Pizza Color has almost no linear relationship with Price and may not be a useful predictor.

---

## When Should We Use Pearson Correlation?

Pearson Correlation is commonly used for:

* Feature Selection
* Data Analysis
* Exploratory Data Analysis (EDA)
* Finding relationships between variables
* Reducing unnecessary features before training a machine learning model

---

## Key Learning

Pearson Correlation tells us **how strongly two variables are related**.

* **+1** means they increase together.
* **-1** means one increases while the other decreases.
* **0** means there is no linear relationship.

It is commonly used before building machine learning models to identify the most useful features and remove those that have little or no relationship with the target variable.
