# elbow
# BDA Lab – Elbow Method for K-Means

This repository contains the dataset and starter code to determine the **optimal number of clusters using the Elbow Method**.

## Objective

Use the **Elbow Method** to find the best number of clusters before applying K-Means.

## Dataset

customers_large_dataset.csv

Features used:

* AnnualIncome
* SpendingScore

## Expected Output

A plot showing:

* X-axis → Number of Clusters (K)
* Y-axis → WCSS (Within Cluster Sum of Squares)

The optimal cluster number is where the **elbow point appears**.


* Upload only inside your folder
* Follow the naming format

### Program:

```
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv("customers_large_dataset.csv")
X = data[["AnnualIncome", "SpendingScore"]]
wcss = []   

for k in range(1, 11): 
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)  

plt.figure()
plt.plot(range(1, 11), wcss)
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()
```

### Output:

<img width="930" height="667" alt="image" src="https://github.com/user-attachments/assets/4419a7fb-813b-45bd-a788-ad459e62cb32" />



