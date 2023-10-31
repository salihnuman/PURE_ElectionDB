import os
import pandas as pd

# Set the folder path
folder_path = 'Source_folder_includes_the_xlsx_files'    # Change the path for your files

# Get a list of all Excel files in the folder
excel_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# Create an empty list to store DataFrames
data_frames = []

# Loop through each Excel file in the folder
for index, file in enumerate(excel_files):
    print(str(index + 1) + " " + file + " is being processed...")
    # Read the Excel file into a DataFrame
    data = pd.read_excel(os.path.join(folder_path, file), skiprows=10)
    data_frames.append(data)

# Concatenate all DataFrames in the list
merged_data = pd.concat(data_frames, ignore_index=False)

# Write the merged data DataFrame to a new Excel file
merged_data.to_excel('The_path_of_created_merged_xlsx_file.xlsx', index=False)    # Change the path for your file
