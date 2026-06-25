import pandas as pd
from sklearn_extra.cluster import KMedoids

df = pd.read_csv("pizza_data.csv")

features = [
    "Company",
    "Pizza Name",
    "Type",
    "Diameter"
]

X = df[features]

X = pd.get_dummies(X)

model = KMedoids(
    n_clusters=4,
    random_state=42
)

model.fit(X)

df["Cluster"] = model.labels_

print(df)
