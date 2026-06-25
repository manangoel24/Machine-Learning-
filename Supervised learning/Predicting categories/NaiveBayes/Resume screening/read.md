# 📄 Resume Screening using Naive Bayes

## Problem Statement

The objective of this project is to classify whether a resume should be **Shortlisted** or **Rejected** using **Naive Bayes**.

Unlike the pizza example, where Naive Bayes was used on structured features such as company, pizza name, type, and diameter, this project applies Naive Bayes to **text data**.

In this project, the model reads resume skills and predicts whether the resume is likely to be shortlisted.

The output is:

* **Shortlisted**
* **Rejected**

---

## Why This Model?

Naive Bayes is commonly used for text classification problems because it works well with word-based data.

In resume screening, the model looks at the words present in a resume, such as skills, tools, programming languages, and technical keywords. Based on the words it has seen during training, it learns which terms are more commonly associated with shortlisted resumes and which terms are more commonly associated with rejected resumes.

This makes Naive Bayes useful for simple text-based classification tasks such as:

* Resume screening
* Spam detection
* Sentiment analysis
* Document classification
* Email filtering

---

## How Does It Make Predictions?

The model first converts resume text into numerical form using **CountVectorizer**.

CountVectorizer counts how often each word appears in the resume text and converts the words into numbers that the Machine Learning model can understand.

After this, the Naive Bayes model learns the probability of certain words appearing in shortlisted resumes and rejected resumes.

For example, if words like **Python**, **Machine Learning**, **SQL**, or **Linear Regression** appear frequently in shortlisted resumes during training, the model may associate these words with the **Shortlisted** class.

When a new resume is entered, the model checks the words in that resume, calculates the probability of each class, and predicts the class with the higher probability.

---

## Technical Implementation

Programming Language: Python

Libraries: Pandas, Scikit-learn

Machine Learning Model: Multinomial Naive Bayes

Text Conversion Method: CountVectorizer

Feature Used: Resume_Text

Target Variable: Result

---

## Model Workflow

Load the resume dataset.

Select **Resume_Text** as the input feature.

Select **Result** as the target variable.

Convert resume text into numerical form using **CountVectorizer**.

Train the Multinomial Naive Bayes model.

Accept resume skills as input from the user.

Convert the entered resume skills into numerical form.

Predict whether the resume should be shortlisted or rejected.

---

## Why Is There a def Function?

In this project, a function called **ResumeScreening()** is used because the goal is not only to train the model but also to test it with custom user input.

The function allows the user to enter resume skills manually. The model then processes the entered text and predicts whether the resume is likely to be shortlisted or rejected.

This makes the project more interactive and closer to a real-world resume screening system.

---

## Example Output

**Input:**

```text
linear regression
```

**Output:**

```text
Prediction: Shortlisted
```

This means the model identified the entered skill as being more closely associated with resumes that were shortlisted in the training data.

---

## How Is It Different From Pizza Purchase Prediction using Naive Bayes?

Both projects use **Naive Bayes**, but they apply it to different types of data.

In the pizza purchase project, Naive Bayes was used on **structured data** such as company, pizza name, pizza type, and diameter.

In this resume screening project, Naive Bayes is used on **text data**. The model does not directly understand words, so the resume text must first be converted into numbers using **CountVectorizer**.

In simple terms:

* **Pizza Naive Bayes** classifies structured pizza data.
* **Resume Naive Bayes** classifies text-based resume data.

This shows that the same algorithm can be used in different ways depending on the type of problem and the type of data.
