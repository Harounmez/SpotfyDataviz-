import panel as pn
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from dataloader import df  # Make sure to adjust the import statement based on your project structure
from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import LabelEncoder

X = df.drop('track_genre', axis=1)
y = df['track_genre']

# Encode labels
encoder = LabelEncoder()
y = encoder.fit_transform(y)

def kmeans_clustering(X, n_clusters):
    # Standardize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Apply K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X_scaled)

    # Calculate Inertia
    inertia = kmeans.inertia_

    # Calculate Silhouette Score
    silhouette_avg = silhouette_score(X_scaled, kmeans.labels_)

    # Assign cluster labels to the original data
    X_labeled = X.copy()
    X_labeled['cluster'] = kmeans.labels_

    return X_labeled, inertia, silhouette_avg

# Example usage:
# Assuming X is your feature matrix and n_clusters is the desired number of clusters
result, inertia, silhouette_avg = kmeans_clustering(X,3)
print(f"Inertia: {inertia}")
print(f"Silhouette Score: {silhouette_avg}")
print(result.head())