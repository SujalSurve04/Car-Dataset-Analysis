import pandas as pd
import matplotlib.pyplot as plt


a = pd.read_csv('Datasettask1.csv') 

# Bar chart for a categorical variable
plt.figure(figsize=(10, 6))
plt.bar(a['CarModel'], a['Price ($)'], color='skyblue')
plt.xlabel('Car Models')
plt.ylabel('Price ($)')
plt.title('Bar Chart - Distribution of Car Prices')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

# Histogram for a continuous variable
plt.figure(figsize=(10, 6))
plt.hist(a['FuelEfficiency'], bins=20, color='orange', edgecolor='black')
plt.xlabel('Fuel Efficiency')
plt.ylabel('Frequency')
plt.title('Histogram - Distribution of Fuel Efficiency')
plt.tight_layout()
plt.show()
