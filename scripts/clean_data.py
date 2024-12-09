import pandas as pd
import os
import glob

# File paths
input_dir = os.path.abspath(os.path.join("data", "raw_copy"))  # Corrected path to raw_copy folder
output_dir = os.path.abspath(os.path.join("data", "cleaned"))  # Corrected path to cleaned folder

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)
print(f"Input directory: {input_dir}")
print(f"Output directory: {output_dir}")

# Get a list of all CSV files in the raw_copy folder
csv_files = glob.glob(os.path.join(input_dir, "*.csv"))
print(f"Files to clean: {csv_files}")

# Loop through each file and clean the data
for file_path in csv_files:
    print(f"Cleaning file: {file_path}")
    
    # Load the CSV file, skipping unnecessary rows (adjust skiprows based on your dataset structure)
    data = pd.read_csv(file_path, skiprows=3)  # Skipping first 3 rows; adjust if needed
    
    # Drop columns that are entirely empty or irrelevant
    data.dropna(how="all", axis=1, inplace=True)
    
    # Rename columns (adjust based on your dataset)
    # This is an example; modify column names as per the actual data structure
    data.columns = [
        "type_of_construction",
        "jan_2024",
        "dec_2023",
        "nov_2023",
        "oct_2023",
        "sep_2023",
        "jan_2023",
        "percent_change_dec",
        "percent_change_jan"
    ]
    
    # Drop rows that are completely empty or contain irrelevant headers
    data = data.dropna(how="all")
    data = data[data["type_of_construction"].notna()]  # Keep only rows with valid "type_of_construction"

    # Handle missing values in numeric columns (replace NaN with 0)
    numeric_columns = data.columns[1:]  # Assuming all columns except the first are numeric
    data[numeric_columns] = data[numeric_columns].fillna(0)
    
    # Save the cleaned data
    file_name = os.path.basename(file_path).replace(".csv", "_cleaned.csv")
    cleaned_file_path = os.path.join(output_dir, file_name)
    data.to_csv(cleaned_file_path, index=False)
    
    # Confirm saving
    if os.path.exists(cleaned_file_path):
        print(f"Cleaned file saved: {cleaned_file_path}")
    else:
        print(f"Failed to save cleaned file: {cleaned_file_path}")

print("Data cleaning completed!")