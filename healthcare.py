import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data Loading and Exploration

# Load the dataset
url = 'path_to_your_dataset.csv'  # Replace with your dataset path
df = pd.read_csv(url)

# Display the first few rows of the dataset
print(df.head())

# Check the data types of each column
print(df.dtypes)

# Summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# 2. Exploring Relationships

# Check the unique values in relevant columns
print(df['year'].unique())
print(df['handwashing'].unique())
print(df['deaths'].unique())
print(df['births'].unique())

# Create a column for mortality rate
df['mortality_rate'] = (df['deaths'] / df['births']) * 100

# Display the first few rows to check the new column
print(df.head())

# 3. Data Calculations

# Separate data before and after handwashing implementation
before_handwashing = df[df['handwashing'] == 'No']
after_handwashing = df[df['handwashing'] == 'Yes']

# Calculate mean mortality rates before and after handwashing
mean_mortality_before = before_handwashing['mortality_rate'].mean()
mean_mortality_after = after_handwashing['mortality_rate'].mean()

print(f"Mean mortality rate before handwashing: {mean_mortality_before:.2f}%")
print(f"Mean mortality rate after handwashing: {mean_mortality_after:.2f}%")

# 4. Data Visualization

# Set the style of the visualization
sns.set(style='whitegrid')

# Line chart showing mortality rates over time
plt.figure(figsize=(14, 8))
sns.lineplot(x='year', y='mortality_rate', data=df, hue='handwashing')
plt.title('Mortality Rate Over Time')
plt.xlabel('Year')
plt.ylabel('Mortality Rate (%)')
plt.legend(title='Handwashing')
plt.show()

# Bar plot comparing mean mortality rates before and after handwashing
mortality_comparison = pd.DataFrame({
    'Period': ['Before Handwashing', 'After Handwashing'],
    'Mean Mortality Rate (%)': [mean_mortality_before, mean_mortality_after]
})

plt.figure(figsize=(8, 6))
sns.barplot(x='Period', y='Mean Mortality Rate (%)', data=mortality_comparison, palette='viridis')
plt.title('Mean Mortality Rate Before and After Handwashing')
plt.xlabel('Period')
plt.ylabel('Mean Mortality Rate (%)')
plt.show()
