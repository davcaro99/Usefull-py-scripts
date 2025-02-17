"""
This script extracts information from all PDF files in a folder and compiles it into a CSV file.
It is designed for organizing book collections by retrieving relevant metadata from PDFs.
"""
if __name__ == "__main__":
    print("PDF Metada ver 0.01")

import os
from PyPDF2 import PdfReader
import pandas as pd
from datetime import datetime

def extract_pdf_metadata(folder_path, csv_path):
    """
    Extract metadata from all PDF files in the specified folder and save to CSV.
    
    Args:
        folder_path (str): Path to the folder containing PDF files
    
    Returns:
        pd.DataFrame: DataFrame containing the metadata
    """
    metadata_list = []


    # Walk through the folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                file_path = os.path.join(root, file)
                try:
                    # Read PDF file
                    with open(file_path, 'rb') as pdf_file:
                        pdf = PdfReader(pdf_file)
                        info = pdf.metadata
                        
                        # Get file info
                        file_stats = os.stat(file_path)
                        
                        # Create metadata dictionary
                        metadata = {
                            'File_Name': file,
                            'File_Size_MB': round(file_stats.st_size / (1024 * 1024), 2),
                            'Last_Modified': datetime.fromtimestamp(file_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                            'Number_of_Pages': len(pdf.pages),
                            'Author': info.get('/Author', ''),
                            'Creator': info.get('/Creator', ''),
                            'Producer': info.get('/Producer', ''),
                            'Subject': info.get('/Subject', ''),
                            'Title': info.get('/Title', ''),
                            'Creation_Date': info.get('/CreationDate', '')
                        }
                        
                        metadata_list.append(metadata)
                        
                except Exception as e:
                    print(f"Error processing {file}: {str(e)}")
    
    # Create DataFrame
    df = pd.DataFrame(metadata_list)
    Ffolder = os.path.split(folder_path)[-1]

    # Save to CSV
    output_file = os.path.join(csv_path, f'{Ffolder}_pdf_metadata.csv')
    df.to_csv(output_file, index=False, encoding='utf-8')
    
    print(f"Metadata saved to: {output_file}")
    return df




# Example usage
folder_path = "D:\Libros\Maths"
#input("Enter the folder path containing PDF files: ")
csv_path = "D:\STRI\STF2024\py\pdf_metadata"
metadata_df = extract_pdf_metadata(folder_path, csv_path)
print("\nFirst few rows of the extracted metadata:")
print(metadata_df.head())

print(metadata_df.describe())