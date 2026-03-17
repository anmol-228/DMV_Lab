import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [20, np.nan, 22, np.nan, 25],
    "Marks": [85, 90, np.nan, 88, np.nan]
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

print("\nMissing Values Count:\n", df.isnull().sum())

df["Age"].fillna(df["Age"].mean(), inplace=True)        # fill with mean
df["Marks"].fillna(df["Marks"].median(), inplace=True)  # fill with median

print("\nAfter Handling Missing Values:\n", df)

sns.heatmap(pd.DataFrame(data).isnull(), cbar=False)
plt.title("Missing Values Heatmap (Before Handling)")
plt.show()

sns.heatmap(df.isnull(), cbar=False)
plt.title("Missing Values Heatmap (After Handling)")
plt.show()