import pandas as pd

# Load the dataset
file_path = 'Telecom Churn.csv'  # Replace with your dataset's file path
telecom_data = pd.read_csv(file_path)

# Extract numerical columns
numerical_data = telecom_data.select_dtypes(include=['float64', 'int64'])

# Iterate through each numerical column and compute statistics
for column in numerical_data.columns:
    print(f"Statistics for column: {column}")
    
    # Minimum value
    min_value = numerical_data[column].min()
    print(f"Minimum: {min_value}")
    
    # Maximum value
    max_value = numerical_data[column].max()
    print(f"Maximum: {max_value}")
    
    # Mean value
    mean_value = numerical_data[column].mean()
    print(f"Mean: {mean_value}")
    
    # Range (Maximum - Minimum)
    range_value = max_value - min_value
    print(f"Range: {range_value}")
    
    # Standard deviation
    std_value = numerical_data[column].std()
    print(f"Standard Deviation: {std_value}")
    
    # Variance
    variance_value = numerical_data[column].var()
    print(f"Variance: {variance_value}")
    
    # 25th Percentile
    percentile_25 = numerical_data[column].quantile(0.25)
    print(f"25th Percentile: {percentile_25}")
    
    # 50th Percentile (Median)
    median_value = numerical_data[column].quantile(0.50)
    print(f"50th Percentile (Median): {median_value}")
    
    # 75th Percentile
    percentile_75 = numerical_data[column].quantile(0.75)
    print(f"75th Percentile: {percentile_75}")
    
    print("-" * 50) 
    print("\n") # Separator for clarity
