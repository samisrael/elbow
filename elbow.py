# Step 1: Import libraries

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Step 2: Load dataset

data = pd.read_csv("dataset/customers_large_dataset.csv")

# Step 3: Select features

X = data[["AnnualIncome", "SpendingScore"]]

# Step 4: Apply Elbow Method

wcss = []

for k in range(1, 11):
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X)
wcss.append(kmeans.inertia_)

# Step 5: Plot the Elbow graph

plt.figure()
plt.plot(range(1, 11), wcss, marker='o')
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.title("Elbow Method")

plt.show()
