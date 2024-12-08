import pandas as pd
import os
import glob

# File paths
data_dir = os.path.abspath(os.path.join("data", "raw"))  # Corrected path to raw folder
output_dir = os.path.abspath(os.path.join("data", "raw_copy"))  # Corrected path to raw_copy folder

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)
print(f"Output directory: {output_dir}")

# Get a list of all Excel files in the raw data folder
excel_files = glob.glob(os.path.join(data_dir, "*.xlsx"))
print(f"Files detected: {excel_files}")

# Loop through each file and save as CSV
for file_path in excel_files:
    print(f"Processing file: {file_path}")
    
    # Load the Excel file
    data = pd.read_excel(file_path)
    
    # Save the data as CSV
    file_name = os.path.basename(file_path).replace(".xlsx", ".csv")
    output_file_path = os.path.join(output_dir, file_name)
    data.to_csv(output_file_path, index=False)
    
    # Confirm saving
    if os.path.exists(output_file_path):
        print(f"File saved: {output_file_path}")
    else:
        print(f"Failed to save: {output_file_path}")

print("Data import completed!")