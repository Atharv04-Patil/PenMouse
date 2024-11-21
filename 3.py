import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'House Data.csv'  # Replace with your dataset's file path
house_data = pd.read_csv(file_path)

# Clean the 'price' column: Remove invalid characters
house_data['price'] = house_data['price'].str.extract('(\d+)').astype(float)

# Clean the 'GrossSquareMeters' column: Remove "m2", strip whitespace, and convert to float
house_data['GrossSquareMeters'] = house_data['GrossSquareMeters'].str.replace("m2", "", regex=False).str.strip()
house_data['GrossSquareMeters'] = pd.to_numeric(house_data['GrossSquareMeters'], errors='coerce')

# Drop rows with missing or invalid values
house_data = house_data.dropna()

# Extract numeric columns
numeric_data = house_data.select_dtypes(include=['float64', 'int64'])

# Compute statistics
print("Standard Deviation:")
for column in numeric_data.columns:
    print(f"{column}: {numeric_data[column].std()}")

print("\nVariance:")
for column in numeric_data.columns:
    print(f"{column}: {numeric_data[column].var()}")

print("\n25th Percentile:")
for column in numeric_data.columns:
    print(f"{column}: {numeric_data[column].quantile(0.25)}")

print("\n50th Percentile (Median):")
for column in numeric_data.columns:
    print(f"{column}: {numeric_data[column].quantile(0.50)}")

print("\n75th Percentile:")
for column in numeric_data.columns:
    print(f"{column}: {numeric_data[column].quantile(0.75)}")

# Generate histograms
print("\nGenerating histograms for each feature...")
numeric_data.hist(bins=20, figsize=(12, 10), edgecolor='black')
plt.tight_layout()
plt.show()


"""
1. Import Required Libraries
    pandas: A library for data manipulation and analysis.
    matplotlib.pyplot: A library for creating static, animated, and interactive visualizations. It's used here for histograms.

2. Load the Dataset
    file_path: The path to the dataset file. Replace this with the actual path where the dataset is stored.
    pd.read_csv(file_path): Reads the dataset into a DataFrame called house_data.


3. Clean the 'price' Column
    house_data['price']: Selects the price column.
    str.extract('(\d+)'): Extracts only numeric parts (digits) from strings in the price column. For example:

        '34550000arrow_downward%3' → '34550000'.

    .astype(float): Converts the extracted string of numbers to a floating-point number.

4. Clean the 'GrossSquareMeters' Column
    house_data['GrossSquareMeters']: Selects the GrossSquareMeters column.
    .str.replace("m2", "", regex=False): Removes the unit "m2" from the column values.
    .str.strip(): Removes any leading or trailing whitespace.
    pd.to_numeric: Converts the column values to numeric data type.
    errors='coerce': Replaces non-convertible values with NaN (Not a Number), indicating missing or invalid data.

5. Drop Rows with Missing or Invalid 
    Valuesdropna(): Removes rows that have missing (NaN) values in any column. Ensures only clean and complete data is retained.

6. Extract Numeric Columns
    select_dtypes(include=['float64', 'int64']): Filters the DataFrame to keep only numeric columns (of types float64 or int64).

7. Compute Statistics
    for column in numeric_data.columns: Iterates through each numeric column.
    numeric_data[column].std(): Computes the standard deviation (a measure of spread) for the column.
    numeric_data[column].var(): Computes the variance (squared deviation from the mean) for the column.
    numeric_data[column].quantile(0.25): Computes the 25th percentile (first quartile).
    Similar logic is used for the 50th (median) and 75th (third quartile) percentiles.

8. Generate Histograms
    numeric_data.hist(bins=20, ...): Generates histograms for all numeric columns in the dataset.
    
    bins=20: Divides the data range into 20 intervals (bins) for the histogram.
    edgecolor='black': Adds a black border around the bars for better visibility.

    plt.tight_layout(): Adjusts spacing between plots to avoid overlapping.
    plt.show(): Displays the histograms.
"""
