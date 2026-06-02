import matplotlib.pyplot as plt

def perform_eda(df):

    plt.figure(figsize=(8,5))
    plt.hist(df['Annual Income (₹)'], bins=10)
    plt.title("Annual Income Distribution")
    plt.xlabel("Income")
    plt.ylabel("Count")
    plt.show()

    plt.figure(figsize=(8,5))
    plt.hist(df['Age'], bins=10)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.show()