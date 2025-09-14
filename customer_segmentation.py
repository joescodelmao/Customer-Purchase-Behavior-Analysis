import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 1. Simulate e-commerce transaction data
np.random.seed(42)
num_records = 100000

data = pd.DataFrame({
    'CustomerID': np.random.randint(1000, 5000, size=num_records),
    'TransactionDate': pd.date_range(start='2022-01-01', periods=num_records, freq='H'),
    'Quantity': np.random.randint(1, 5, size=num_records),
    'UnitPrice': np.random.uniform(5, 200, size=num_records)
})

data['Revenue'] = data['Quantity'] * data['UnitPrice']

# 2. Clean anomalies
# Remove negative or zero values (if any)
data = data[(data['Quantity'] > 0) & (data['UnitPrice'] > 0)]

# Drop potential duplicates
data.drop_duplicates(inplace=True)

# 3. Aggregate customer-level features for clustering
customer_df = data.groupby('CustomerID').agg({
    'Revenue': 'sum',
    'Quantity': 'sum',
    'TransactionDate': 'count'  # number of purchases
}).rename(columns={'TransactionDate': 'NumPurchases'}).reset_index()

# 4. Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(customer_df[['Revenue', 'Quantity', 'NumPurchases']])

# 5. KMeans clustering
kmeans = KMeans(n_clusters=4, random_state=42)
customer_df['Cluster'] = kmeans.fit_predict(X_scaled)

# 6. Visualization of clusters
plt.figure(figsize=(8,6))
sns.scatterplot(
    data=customer_df,
    x='Revenue',
    y='NumPurchases',
    hue='Cluster',
    palette='Set2',
    alpha=0.7
)
plt.title('Customer Segmentation by Revenue and Purchases')
plt.xlabel('Total Revenue')
plt.ylabel('Number of Purchases')
plt.show()

# 7. Export for Tableau
customer_df.to_csv('customer_segments.csv', index=False)

print(customer_df.head())
