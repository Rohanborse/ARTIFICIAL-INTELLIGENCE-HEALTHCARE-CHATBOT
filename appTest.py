
import os
import pandas as pd

current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

file_name = r"Code\dataset.xlsx"  # Replace with the actual file name
if os.path.exists(file_name):
    # The file exists, proceed with reading it
    print("File exists.")
else:
    print("File does not exist.")

try:
    df = pd.read_excel(file_name, engine='openpyxl')
    print(df)
except FileNotFoundError as e:
    print(f"File not found: {e}")
except Exception as e:
    print(f"An error occurred: {e}")