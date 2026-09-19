# AI & Machine Learning

## Overview
This repository documents my learning journey in Artificial Intelligence and Machine Learning, covering Python fundamentals, data structures, supervised and unsupervised learning techniques, and practical projects.

## Topics

### Python Fundamentals
- Variables and data types
- Operators and expressions
- Control flow (if/else, loops)
- Functions and modules

### Data Structures & Algorithms
- Lists, dictionaries, and basic data structures
- Searching and sorting algorithms

### Supervised Learning
- **Linear Regression**
- **Logistic Regression** – binary classification (e.g., heart disease, employee turnover)
- **Decision Trees** – classifier and regressor implementations
- **K-Nearest Neighbors (KNN)** – classification and regression
- **Naive Bayes** – probabilistic classifiers
- **Random Forest** – ensemble methods (if implemented)

### Unsupervised Learning
#### Clustering
- **K-Means Clustering** – basic implementation and applications on Iris dataset
- **DBSCAN** – density‑based clustering and anomaly detection
- **Hierarchical Clustering** – agglomerative methods
- **Isolation Forest** – anomaly detection algorithm

#### Dimensionality Reduction
- **Principal Component Analysis (PCA)** – variance preservation and feature extraction

### Feature Engineering & Preprocessing
- Data cleaning and handling missing values
- Encoding categorical variables
- Feature scaling and transformation

## Projects
- **SmartCart Customer Segmentation** – K‑Means clustering for segmenting customer data
- **Explainable AI for Cancer Prediction (Research)** – interpretability techniques for healthcare models
- **Credit Wise Loan System** – loan approval prediction using logistic regression and preprocessing
- **Anomaly Detection in Financial Transactions** – Isolation Forest for fraud detection
- **Clustering of Iris Dataset** – comparative analysis of K‑Means, DBSCAN, and hierarchical clustering

## Repository Structure
```
python/
├── python basic/           # Python fundamentals
├── Data structure/         # Data structures and algorithms
├── Supervised ML/
│   ├── KNN/                # K‑Nearest Neighbors
│   ├── naive bayes/        # Naive Bayes classifier
│   ├── logistic regression/# Logistic regression + assignments
│   └── decision tree/      # Decision tree classifier & regressor
└── Unsupervised Learning/
    ├── clustering/         # All clustering algorithms
    │   ├── DBSCAN.ipynb
    │   ├── KMeans.ipynb
    │   ├── KMeansForIris.ipynb
    │   ├── PCA.ipynb
    │   ├── clustering_DBSCAN.ipynb
    │   ├── hierarchical_clustering.ipynb
    │   ├── isolation_forest.ipynb
    │   └── thyroid_dataset.csv
    └── Dimensionality Reduction/
        └── PCA.ipynb
```