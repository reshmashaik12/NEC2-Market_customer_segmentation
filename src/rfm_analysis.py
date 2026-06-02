def rfm_analysis(df):

    print("\nRFM Analysis")

    rfm = df[['CustomerID',
              'Annual Income (₹)',
              'Spending Score']]

    print(rfm.head())

    return rfm