# 🎬 Movie Recommendation System using K-Nearest Neighbors (KNN)

## Overview

This project demonstrates another practical application of **K-Nearest Neighbors (KNN)**.

Instead of classifying pizzas as **Bought** or **Not Bought**, we can also do this - KNN is used to recommend movies that are similar to a movie selected by the user.

The idea behind the recommendation system is simple:

> **If two movies receive similar ratings from many users, they are likely to be similar.**

For example, if a user likes **Vampires**, the model searches the dataset for movies that have similar rating patterns and recommends the closest matches.

---

## Why This Project?

Most people first learn KNN as a **classification algorithm**, where it predicts a category based on the nearest neighbors.

However, KNN can also be used for **recommendation systems** by measuring similarity between items instead of predicting a class.

This project demonstrates how the same algorithm can solve a completely different problem simply by changing what "neighbor" means.

---

## How Does It Make Recommendations?

Every movie receives ratings from many users.

Movies that receive similar rating patterns are considered similar.

The model first creates a matrix where:

* Rows represent movies.
* Columns represent users.
* Each value represents a user's rating for a movie.

When a movie is entered, KNN compares its rating pattern with every other movie in the dataset using **Cosine Similarity**.

It then finds the closest neighboring movies and recommends them to the user.

Unlike KNN Classification, no category is predicted. Instead, the algorithm simply returns the movies that are most similar to the selected movie.

---

## Technical Implementation

Programming Language: Python

Libraries: Pandas, Scikit-learn

Machine Learning Model: K-Nearest Neighbors

Similarity Measure: Cosine Similarity

Input: Movie Name

Output: Recommended Movies

---

## Model Workflow

Load the movie dataset and the user ratings dataset.

Merge both datasets using the Movie ID.

Create a movie-user rating matrix using a Pivot Table.

Replace missing ratings with **0**.

Train a K-Nearest Neighbors model using **Cosine Similarity**.

When a movie is entered, find the nearest neighboring movies.

Display the most similar movie recommendations.

---

## Example

**Input Movie:**

Vampires

**Recommended Movies:**

* Fright Night
* The Faculty
* Arachnophobia
* Lord of Illusions
* Bram Stoker's Dracula

These recommendations are generated because the users who rated **Vampires** gave similar ratings to these movies.

---

## What We Learned

This project shows that **KNN is not limited to classification problems.**

The same algorithm can also be used to build recommendation systems by finding the most similar items in a dataset.

Rather than predicting a category or a numerical value, KNN searches for the nearest neighbors based on similarity and returns the closest matches.

This is the same idea used by many recommendation systems in movies, music, shopping platforms, and streaming services.

---

## How Is It Different From KNN Classification?

Although both projects use the **K-Nearest Neighbors (KNN)** algorithm, they solve different types of problems.

**KNN Classification** predicts a category, such as whether a customer will **Buy** or **Not Buy** a pizza.

**KNN Recommendation** does not predict a category. Instead, it searches for the most similar items based on user behavior and returns recommendations.

In simple terms:

* **KNN Classification** → Predicts a category (Buy / Not Buy)
* **KNN Recommendation** → Finds the most similar items

This demonstrates how the same algorithm can solve different kinds of problems simply by changing what "neighbor" represents.
