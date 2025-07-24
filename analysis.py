import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Category': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'Value1': [10, 15, 20, 12, 18, 22, 11, 16, 21, 13, 19, 23, 14, 17, 24],
    'Value2': [100, 150, 200, 120, 180, 220, 110, 160, 210, 130, 190, 230, 140, 170, 240]
}

df = pd.DataFrame(data)

display(df.head())
display(df.info())

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.bar(df['Category'], df['Value1'])
plt.xlabel('Category')
plt.ylabel('Value1')
plt.title('Bar Chart of Value1 by Category')
plt.show()

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Value1'], df['Value2'])
plt.xlabel('Value1')
plt.ylabel('Value2')
plt.title('Scatter Plot of Value1 vs. Value2')
plt.show()
