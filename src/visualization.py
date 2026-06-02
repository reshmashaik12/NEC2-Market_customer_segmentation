import matplotlib.pyplot as plt

def visualize_clusters(pca_data, clusters):

    plt.figure(figsize=(8,6))

    plt.scatter(
        pca_data[:,0],
        pca_data[:,1],
        c=clusters
    )

    plt.title("Customer Segments")
    plt.xlabel("PCA 1")
    plt.ylabel("PCA 2")

    plt.show()