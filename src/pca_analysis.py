from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def perform_pca(df):

    features = df[['Age',
                   'Annual Income (₹)',
                   'Spending Score']]

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(features)

    pca = PCA(n_components=2)

    pca_data = pca.fit_transform(scaled_data)

    return pca_data, scaled_data