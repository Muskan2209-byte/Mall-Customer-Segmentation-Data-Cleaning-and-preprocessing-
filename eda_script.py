Once EDA is done, you can run K-Means Clustering to segment customers into groups (e.g., low spenders, high income etc)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv('mall_customers_cleaned.csv')

# Set style for seaborn
sns.set(style='whitegrid')

# 1. Basic Info
print("Dataset Info:\n", df.info())
print("\nSummary Stats:\n", df.describe())

# 2. Gender Distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='gender')
plt.title('Gender Distribution')
plt.savefig('gender_distribution.png')
plt.close()

# 3. Age Distribution
plt.figure(figsize=(8, 4))
sns.histplot(df['age'], bins=10, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.savefig('age_distribution.png')
plt.close()

# 4. Annual Income Distribution
plt.figure(figsize=(8, 4))
sns.histplot(df['annual_income_k$'], bins=10, kde=True, color='green')
plt.title('Annual Income Distribution')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Count')
plt.savefig('income_distribution.png')
plt.close()

# 5. Spending Score Distribution
plt.figure(figsize=(8, 4))
sns.histplot(df['spending_score_1_100'], bins=10, kde=True, color='orange')
plt.title('Spending Score Distribution')
plt.xlabel('Spending Score (1-100)')
plt.ylabel('Count')
plt.savefig('spending_distribution.png')
plt.close()

# 6. Income vs Spending Score Scatter
plt.figure(figsize=(6, 6))
sns.scatterplot(data=df, x='annual_income_k$', y='spending_score_1_100', hue='gender')
plt.title('Income vs Spending Score')
plt.savefig('income_vs_spending.png')
plt.close()

# 7. Age vs Spending Score
plt.figure(figsize=(6, 6))
sns.scatterplot(data=df, x='age', y='spending_score_1_100', hue='gender')
plt.title('Age vs Spending Score')
plt.savefig('age_vs_spending.png')
plt.close()

print("EDA completed and plots saved as PNG files.")
