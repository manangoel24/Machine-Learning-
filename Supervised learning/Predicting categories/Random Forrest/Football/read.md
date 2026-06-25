# ⚽ Football Match Prediction using Random Forest Classification

## Problem Statement

The objective of this project is to predict **whether football can be played or not** using a **Random Forest Classifier**.

Instead of using a single Decision Tree, this project uses multiple decision trees to make a more reliable prediction.

The model predicts whether football should be played based on weather conditions.

The input features are:

* Weather
* Temperature
* Humidity
* Wind

The output is binary:

* **Yes → Football can be played**
* **No → Football should not be played**

---

## Why This Model?

A Decision Tree makes predictions using one tree of rules. While it is simple and easy to understand, it can sometimes memorize the training data too closely.

Random Forest improves this by building many decision trees instead of one.

Each tree makes its own prediction, and the final decision is based on the majority vote of all the trees. This usually leads to more stable and accurate predictions.

---

## How Does It Make Predictions?

Random Forest creates multiple decision trees from the training data.

Each tree learns slightly different decision rules because it is trained on different subsets of the data.

When new weather conditions are entered, every tree predicts whether football should be played.

For example:

* Tree 1 → Yes
* Tree 2 → Yes
* Tree 3 → No
* Tree 4 → Yes
* Tree 5 → Yes

Since most trees predict **Yes**, the Random Forest gives the final prediction:

**Yes → Football can be played**

This process is called **majority voting**.

---

## Technical Implementation

Programming Language: Python

Libraries: Pandas, Scikit-learn, Matplotlib

Machine Learning Model: Random Forest Classifier

Features Used:

Weather
Temperature
Humidity
Wind

Target Variable: PlayFootball

---

## Model Workflow

Load the football dataset.

Convert categorical values into numerical values.

Select the input features.

Train the Random Forest Classifier using multiple decision trees.

Accept weather conditions from the user.

Predict whether football should be played.

Evaluate the model using accuracy.

Visualize one of the trees from the Random Forest.

---

## Why Is There a `def` Function?

Unlike the previous Random Forest Classification example, this project is designed to predict new weather conditions entered by the user.

The **PlayFootball()** function accepts the weather information, converts the inputs into numerical values using the mapping dictionary, and sends them to the trained Random Forest model.

The model then predicts whether football should be played.

This makes the project interactive and demonstrates how a trained Random Forest model can be used in a real-world application.

---

## Model Performance

The Random Forest Classifier achieved an **accuracy of 100%** on this dataset.

This means the model correctly classified all training examples.

However, since the accuracy is calculated on the same data used for training, this perfect score does not necessarily mean the model will perform equally well on new unseen data.

To properly evaluate the model, a train-test split or cross-validation should also be used.

---

## Random Forest Visualization

Unlike a Decision Tree, a Random Forest contains many decision trees.

Visualizing all of them would make the model difficult to understand, so in this project we display **one tree** from the forest.

This visualization helps us understand how one of the trees learned to classify the weather conditions.

Although each tree is slightly different, the final prediction is made by combining the predictions from all the trees through majority voting.

---

## Example Prediction

**Example Input:**

* Weather → Sunny
* Temperature → Hot
* Humidity → High
* Wind → Weak

**Output:**

```text
No, you should not play football.
```

The Random Forest checks the predictions from all of its trees and returns the majority decision.

---

## How Is It Different From Football Prediction using Decision Tree?

Both projects predict whether football should be played using the same weather features.

The difference lies in how they make their decisions.

A **Decision Tree** uses one tree of rules to make a prediction.

A **Random Forest** builds many different decision trees and combines their predictions using majority voting.

In simple terms:

* **Decision Tree asks:** *"What does this one tree predict?"*
* **Random Forest asks:** *"What do most of my trees predict?"*

Because it combines many trees, Random Forest is generally more stable and less likely to overfit than a single Decision Tree.
