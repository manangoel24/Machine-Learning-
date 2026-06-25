# ⚽ Football Match Prediction using Decision Tree

## Problem Statement

The objective of this project is to predict **whether football can be played or not** using a **Decision Tree Classifier**.

Instead of predicting whether a customer will buy a pizza, this project demonstrates how Decision Trees can be applied to a completely different problem.

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

## Why This Example?

Decision Trees are easiest to understand when we can actually see the questions they ask.

Using weather conditions makes the decision-making process intuitive because people naturally make decisions like:

* Is it raining?
* Is the humidity high?
* Is the wind too strong?

The Decision Tree learns these kinds of rules automatically from historical data and uses them to make future predictions.

---

## How Does It Make Predictions?

The Decision Tree starts from the root of the tree and asks one question at a time.

For example:

* Is the humidity high?
* If not, what is the weather?
* If it is sunny, how strong is the wind?

Based on the answer to each question, the model follows a branch until it reaches a final leaf node.

The leaf node contains the prediction:

* **Yes → Play Football**
* **No → Do Not Play Football**

Unlike algorithms that rely on mathematical equations or probabilities, Decision Trees make predictions using a sequence of simple rules.

---

## Technical Implementation

Programming Language: Python

Libraries: Pandas, Scikit-learn, Matplotlib

Machine Learning Model: Decision Tree Classifier

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

Select the input features (Weather, Temperature, Humidity, and Wind).

Train the Decision Tree Classifier.

Accept weather conditions from the user.

Predict whether football should be played.

Visualize the trained decision tree.

---

## Why Is There a `def` Function?

Unlike the previous Decision Tree project, this example is designed to make predictions for new weather conditions entered by the user.

The **PlayFootball()** function accepts the weather conditions, passes them to the trained model, and displays whether football should be played.

This makes the project interactive and demonstrates how a trained Decision Tree can be used in a real-world application.

---

## Decision Tree Visualization

One of the biggest advantages of Decision Trees is that we can visualize exactly how the model makes decisions.

The generated tree shows:

* The question asked at each node
* How the dataset is split
* The number of training samples at each node
* The predicted class at every leaf node

Unlike many other Machine Learning algorithms, Decision Trees are highly interpretable because we can follow every decision from the root to the final prediction.

---

## Example Prediction

**Example Input:**

* Weather → Sunny
* Temperature → Hot
* Humidity → Normal
* Wind → Weak

**Output:**

```text
Prediction: Yes, you can play football
```

The model follows the decision tree and predicts whether the weather conditions are suitable for playing football.

---

## How Is It Different From Pizza Purchase Prediction?

Both projects use the **Decision Tree Classifier**, but they solve different problems.

In the pizza project, the model predicts whether a customer will **Buy** or **Not Buy** a pizza.

In this project, the model predicts whether football should be **Played** or **Not Played** based on weather conditions.

Although the datasets are different, the learning process remains exactly the same. The Decision Tree learns a series of rules from the training data and follows those rules to make predictions on new inputs.

This demonstrates that the same algorithm can be applied to many different classification problems simply by changing the dataset.
