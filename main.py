from src.data_preprocessing import load_data
from src.eda import perform_eda
from src.rfm_analysis import rfm_analysis
from src.pca_analysis import perform_pca
from src.clustering import perform_clustering
from src.visualization import visualize_clusters

# Load Dataset
df = load_data()

# EDA
perform_eda(df)

# RFM Analysis
rfm_analysis(df)

# PCA
pca_data, scaled_data = perform_pca(df)

# Clustering
df, clusters = perform_clustering(df, scaled_data)

# Visualization
visualize_clusters(pca_data, clusters)

# Save Output
df.to_csv("outputs/customer_clusters.csv", index=False)

print("\nProject Completed Successfully")