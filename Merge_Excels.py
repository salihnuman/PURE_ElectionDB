import os
import pandas as pd

# Set the folder path
folder_path = 'D:/SU/4 - Senior/Fall/PURE/Seçimler/4 - 31 MART 2019 MAHALLİ İDARELER GENEL SEÇİMİ (31.03.2019) SONUÇLARI/BÜYÜKŞEHİR BELEDİYE BAŞKANLIĞI SEÇİMLERİ'

# Get a list of all Excel files in the folder
excel_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# Create an empty list to store DataFrames
data_frames = []
index = 0


# data = pd.read_excel(os.path.join(folder_path, excel_files[0]), skiprows=10)

# data2 = pd.read_excel(os.path.join(folder_path, excel_files[1]), skiprows=10)
# data_frames = pd.concat([data, data2], ignore_index=True)
# # print(data)
# print(data_frames)

# Loop through each Excel file in the folder
for index, file in enumerate(excel_files):
    print(str(index + 1) + " " + file + " is being processed...")
    # Read the Excel file into a DataFrame
    data = pd.read_excel(os.path.join(folder_path, file), skiprows=10)
    data_frames.append(data)

# Concatenate all DataFrames in the list
merged_data = pd.concat(data_frames, ignore_index=False)


# print(merged_data.head())  # Display the first 5 rows
# print(merged_data.info())  # Display summary information about the DataFrame

# # Write the merged data DataFrame to a new Excel file
merged_data.to_excel('D:/SU/4 - Senior/Fall/PURE/Seçimler/4 - 31 MART 2019 MAHALLİ İDARELER GENEL SEÇİMİ (31.03.2019) SONUÇLARI Ziplenmiş/BÜYÜKŞEHİR BELEDİYE BAŞKANLIĞI SEÇİMLERİ.xlsx', index=False)
