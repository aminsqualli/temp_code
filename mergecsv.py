import os
import pandas as pd

# Set the maximum number of lines per output CSV file
max_lines_per_file = 1000000

# Function to merge CSV files
def merge_csv_files(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Initialize variables
    total_lines = 0
    file_count = 1
    output_csv_path = os.path.join(output_folder, f"merged_{file_count}.csv")
    output_csv = pd.DataFrame()

    # Loop through CSV files in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.csv'):
            file_path = os.path.join(input_folder, file_name)
            input_csv = pd.read_csv(file_path)

            # Check if adding the current file exceeds the maximum lines per file
            if total_lines + len(input_csv) > max_lines_per_file:
                # Write the current output to a new CSV file
                output_csv.to_csv(output_csv_path, index=False)
                # Reset variables for the next output CSV file
                file_count += 1
                total_lines = 0
                output_csv_path = os.path.join(output_folder, f"merged_{file_count}.csv")
                output_csv = pd.DataFrame()

            # Add current CSV to the output
            output_csv = pd.concat([output_csv, input_csv], ignore_index=True)
            total_lines += len(input_csv)

    # Write the last output to a CSV file
    output_csv.to_csv(output_csv_path, index=False)

# Specify input and output folders
input_folder = 'input_folder_path'
output_folder = 'output_folder_path'

# Call the function to merge CSV files
merge_csv_files(input_folder, output_folder)