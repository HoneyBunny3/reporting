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
    
    # Load the CSV file
    data = pd.read_csv(file_path)
    
    # Standardize column names
    data.columns = [col.strip().lower().replace(" ", "_") for col in data.columns]
    
    # Handle missing values
    data.fillna(0, inplace=True)
    
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