# 🎓 Student Pass Prediction using Support Vector Machine (SVM)

## Problem Statement

The objective of this project is to predict **whether a student will pass or not** using a **Support Vector Machine (SVM)** classifier.

Instead of predicting whether a customer will buy a pizza, this project applies SVM to a student performance dataset.

The model predicts whether a student is likely to pass based on academic and attendance-related features.

The input features are:

* Study Hours
* Attendance
* Previous Score
* Practice Tests

The output is binary:

* **0 → Student will not pass**
* **1 → Student will pass**

---

## Why This Example?

SVM is easier to understand when we can visualize how it separates two groups.

In this example, the model tries to separate students into two classes:

* Students likely to pass
* Students likely to fail

This helps us understand the main idea behind SVM: finding the best boundary that separates different classes as clearly as possible.

---

## How Does It Make Predictions?

SVM tries to draw the best possible boundary between two classes.

In this project, the model looks at student-related features such as study hours, attendance, previous score, and practice tests.

Based on these features, it learns where the boundary should be placed between students who passed and students who did not pass.

When a new student record is given, the model checks which side of the boundary the student falls on.

* If the student falls on the pass side, the model predicts **Pass**.
* If the student falls on the fail side, the model predicts **Fail**.

The points closest to the boundary are called **support vectors**. These points are important because they help decide the position of the boundary.

---

## Technical Implementation

Programming Language: Python

Libraries: Pandas, Scikit-learn, Matplotlib

Machine Learning Model: Support Vector Classifier (SVC)

Features Used:

Study Hours
Attendance
Previous Score
Practice Tests

Target Variable: Passed

---

## Model Workflow

Load the student dataset.

Select the input features.

Select **Passed** as the target variable.

Train the SVM classifier.

Evaluate the model using accuracy.

Visualize the SVM decision boundary using study hours and attendance.

---

## Model Performance

The SVM model achieved an **accuracy of 71%**.

This means the model correctly classified around **71% of the students** as either passed or not passed.

The accuracy shows that SVM was able to learn a useful boundary between the two classes, but there is still room for improvement.

---

## SVM Visualization

The graph shows how SVM separates the students into two groups using a decision boundary.

In the visualization:

* One side of the boundary represents students predicted to pass.
* The other side represents students predicted not to pass.
* The circled points are the **support vectors**.

Support vectors are the most important points for SVM because they lie closest to the boundary and help decide where the separation line should be placed.

This makes the graph useful for understanding how SVM thinks while making classification decisions.

---

## How Is It Different From Pizza Purchase Prediction using SVM?

Both projects use the **Support Vector Machine classifier**, but they apply it to different datasets.

In the pizza project, SVM predicts whether a customer will buy a pizza based on pizza-related information.

In this project, SVM predicts whether a student will pass based on academic and attendance-related information.

The core idea remains the same:

> **SVM tries to find the best boundary that separates two classes.**

This example makes the boundary easier to understand because the visualization clearly shows how the model separates students into pass and fail groups.
