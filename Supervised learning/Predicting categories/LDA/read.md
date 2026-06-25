Pizza Purchase Prediction using Linear Discriminant Analysis (LDA)

## 🍕 Problem Statement

The objective of this project is to predict **whether a customer will buy a pizza or not** using **Linear Discriminant Analysis (LDA)**.

The model learns from previous customer purchase data and predicts whether a new customer is likely to purchase a pizza.

The input features are:

- Company
- Pizza Name
- Type
- Diameter

The output is binary:

- **0 → Customer will not buy**
- **1 → Customer will buy**

---

## 🍕 Why This Example?

Unlike Logistic Regression or SVM, LDA does not simply try to separate the classes.

Instead, it creates a **new feature (called a Linear Discriminant)** by combining the existing features into a single value that separates the classes as much as possible.

The idea is to make customers who buy pizza and customers who do not buy pizza appear farther apart.

---

## 🍕 How Does LDA Create a New Feature?

Suppose we only have two features:

- Diameter
- Cheese

Instead of using both separately, LDA combines them into one new feature.

Imagine LDA learns the following equation:

```
New Feature = 2 × Diameter + 3 × Cheese
```

### Pizza 1

Diameter = 8

Cheese = 2

```
New Feature = 2 × 8 + 3 × 2

            = 16 + 6

            = 22
```

### Pizza 2

Diameter = 15

Cheese = 7

```
New Feature = 2 × 15 + 3 × 7

            = 30 + 21

            = 51
```

Originally the data looked like this:

| Diameter | Cheese |
|----------|---------|
| 8 | 2 |
| 15 | 7 |

After applying LDA, it becomes:

| New Feature |
|-------------|
| 22 |
| 51 |

Now the classes become much easier to separate.

```
No Purchase        Purchase
     22               51
```

This new feature helps LDA build a better decision boundary between the two classes.

---

## 🍕 How Does It Make Predictions?

LDA first studies all the training data.

It learns how the features differ between customers who purchased pizza and those who did not.

Instead of treating every feature separately, it combines them into a new feature that maximizes the separation between the two classes.

When a new pizza record is provided, the model calculates its new feature value and predicts whether it belongs to:

- Customer will buy
- Customer will not buy

---

## 🍕 Technical Implementation

**Programming Language:** Python

**Libraries:** Pandas, Scikit-learn

**Machine Learning Model:** Linear Discriminant Analysis (LDA)

**Features Used:**

- Company
- Pizza Name
- Type
- Diameter

**Target Variable:** Bought

---

## 🍕 Model Workflow

1. Load the pizza dataset.
2. Convert categorical columns into numerical values.
3. Select the input features.
4. Train the Linear Discriminant Analysis model.
5. Evaluate the model using accuracy.
6. Use the trained model to classify pizza purchases.

---

## 🍕 Model Performance

The LDA model achieved an **accuracy of approximately 89%**.

This means the model correctly classified around **89% of the pizza purchase records**.

The high accuracy shows that the transformed feature created by LDA was able to separate customers who purchased pizza from those who did not.

---

## 🍕 How Is It Different From Logistic Regression?

Both Logistic Regression and LDA are classification algorithms.

However, they work differently.

**Logistic Regression**

- Directly learns the probability of each class.
- Creates a decision boundary for classification.

**Linear Discriminant Analysis**

- First creates a new feature by combining the original features.
- Maximizes the separation between classes.
- Then performs classification using this transformed feature.

In simple words:

- Logistic Regression learns **where to draw the boundary.**
- LDA first **transforms the data to make the boundary easier to draw.**
