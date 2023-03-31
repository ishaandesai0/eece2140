import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier

class KMeansClassifier:
    """Implements the unsupervised K-means classification algorithm.
    
    Attributes:
        n_clusters (int): The number of clusters to generate.
        data (np.array): The data to cluster.
        centroids (np.array): The centroids of the clusters.
        labels (np.array): The labels of the clusters.
    """
    def __init__(self, n_clusters, data):
        self.n_clusters = n_clusters
        self.data = data
        self.centroids = None
        self.labels = None
        
    def fit(self):
        """Fits the K-means model to the data."""
        # Randomly initialize the centroids
        self.centroids = self._init_centroids(self.data, self.n_clusters)
        
        # Iteratively update the centroids and labels
        for _ in range(20): # Maximum number of iterations
            self.labels = self._assign_labels(self.data, self.centroids)
            self.centroids = self._update_centroids(self.data, self.labels, self.centroids)
            # Break if the centroids don't change
            if np.array_equal(self.centroids_prev, self.centroids):
                break
            self.centroids_prev = self.centroids.copy()
            
    def _init_centroids(self, data, n_clusters):
        """Randomly initializes the centroids of the clusters."""
        n_features = data.shape[1]
        centroids = np.zeros((n_clusters, n_features))
        for i in range(n_clusters):
            centroid = np.random.uniform(low=np.min(data), high=np.max(data), size=n_features)
            centroids[i] = centroid
        return centroids
    
    def _assign_labels(self, data, centroids):
        """Assigns labels to the data points based on the centroids."""
        labels = []
        for x in data:
            # Compute the distance from the data point to each centroid
            distances = [np.linalg.norm(x - c) for c in centroids]
            # Assign the label of the closest centroid
            label = np.argmin(distances)
            labels.append(label)
        return labels
    
    def _update_centroids(self, data, labels, centroids):
        """Updates the centroids based on the data points and labels."""
        n_clusters = centroids.shape[0]
        for i in range(n_clusters):
            # Get all the data points with the same label
            cluster_data = data[labels == i]
            # Compute the mean of the data points
            centroid = np.mean(cluster_data, axis=0)
            centroids[i] = centroid
        return centroids
    
    def plot_clusters(self):
        """Plots the clusters and centroids."""
        fig, ax = plt.subplots()
        # Plot the data points
        for i in range(self.n_clusters):
            cluster_data = self.data[self.labels == i]
            ax.scatter(cluster_data[:, 0], cluster_data[:, 1], label=f'Cluster {i+1}')
        # Plot the centroids
        ax.scatter(self.centroids[:, 0], self.centroids[:, 1], marker='*', color='k', s=200, label='Centroid')
        ax.set_title('K-means Clustering')
        ax.legend()
        plt.show()
    
class KNearestNeighborClassifier:
    """Implements the supervised K-nearest neighbor classification algorithm.
    
    Attributes:
        n_neighbors (int): The number of neighbors to use for classification.
        data (np.array): The training data.
        labels (np.array): The labels of the training data.
    """
    def __init__(self, n_neighbors, data, labels):
        self.n_neighbors = n_neighbors
        self.data = data
        self.labels = labels
        
    def fit(self):
        """Fits the K-nearest neighbor model to the data."""
        pass
    
    def predict(self, x):
        """Predicts the label of a given data point."""
        # Compute the distance from the data point to each training point
        distances = [np.linalg.norm(x - d) for d in self.data]
        # Get the indices of the n_neighbors closest points
        sorted_indices = np.argsort(distances)[:self.n_neighbors]
        # Get the labels of the closest points
        nearest_labels = self.labels[sorted_indices]
        # Get the most common label
        label = np.bincount(nearest_labels).argmax()
        return label
    
    def plot_clusters(self):
        """Plots the training data and the classification boundary."""
        # Get the min and max values of the data
        x_min, x_max = np.min(self.data[:, 0]), np.max(self.data[:, 0])
        y_min, y_max = np.min(self.data[:, 1]), np.max(self.data[:, 1])
        
        # Create a grid of points
        xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                             np.arange(y_min, y_max, 0.1))
        # Predict the labels for each point
        Z = np.array([self.predict(np.array([x, y])) for x, y in zip(xx.ravel(), yy.ravel())])
        Z = Z.reshape(xx.shape)
        
        fig, ax = plt.subplots()
        # Plot the data points
        for label in np.unique(self.labels):
            cluster_data = self.data[self.labels == label]
            ax.scatter(cluster_data[:, 0], cluster_data[:, 1], label=f'Label {label}')
        # Plot the classification boundary
        ax.contourf(xx, yy, Z, alpha=0.3)
        ax.set_title('K-nearest Neighbor Classification')
        ax.legend()
        plt.show()

class ClassificationModels:
    def __init__(self):
        self.data = None
        self.kmeans_model = None
        self.knn_model = None
        self.k = None
    
    def fit_kmeans(self, data, k):
        self.data = data
        self.k = k
        self.kmeans_model = KMeans(n_clusters=k).fit(data)
        return self.kmeans_model
    
    def plot_kmeans(self):
        if self.kmeans_model is None:
            print('KMeans Model is not fitted!')
            return
        
        plt.scatter(self.data[:, 0], self.data[:, 1], c=self.kmeans_model.labels_, cmap='rainbow')
        plt.title('K-Means Clustering with K = {}'.format(self.k))
        plt.show()
        
    def fit_knn(self, data, labels, k):
        self.data = data
        self.k = k
        self.knn_model = KNeighborsClassifier(n_neighbors=k).fit(data, labels)
        return self.knn_model
    
    def plot_knn(self):
        if self.knn_model is None:
            print('KNN Model is not fitted!')
            return
        
        plt.scatter(self.data[:, 0], self.data[:, 1], c=self.knn_model.predict(self.data), cmap='rainbow')
        plt.title('K-Nearest Neighbor with K={}'.format(self.k))
        plt.show()

# Generate sample data
np.random.seed(100)
data = np.random.rand(100, 2)
labels = np.random.randint(low = 0, high = 2, size = 100)

# Create an instance of the class
clf_model = ClassificationModels()

# Fit and plot the KMeans model
kmeans_model = clf_model.fit_kmeans(data, 10)
clf_model.plot_kmeans()

# Fit and plot the KNN model
knn_model = clf_model.fit_knn(data, labels, 5)
clf_model.plot_knn()
