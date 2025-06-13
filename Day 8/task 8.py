import pandas as pd

# Load the dataset
df = pd.read_csv(r"Sample - Superstore.csv", encoding='latin1')

# Preview the data
print(df.shape)
print(df.head())

# Remove duplicates
df = df.drop_duplicates()

# Rename columns
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Save cleaned dataset
df.to_csv("cleaned_superstore.csv", index=False)
print("Cleaning complete. Cleaned data saved as cleaned_superstore.csv.")
