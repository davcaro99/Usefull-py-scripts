"""
This script processes a PDF list of georeferenced localities, 
extracting details such as coordinates, names, measurements, and comments into a CSV file. 
The data can be modified and used to generate a KMZ file with all information, including images.
The user can modify the information in the script according to the information in the pdf file.
"""

import pdfplumber
import pandas as pd
import re

def extract_pdf_data(pdf_path):
    """
    Extract data from PDF file and return as a list of dictionaries.
    """
    extracted_data = []
    
    with pdfplumber.open(pdf_path) as pdf:
        print(f"Processing PDF with {len(pdf.pages)} pages...")
        
        for page_num, page in enumerate(pdf.pages, 1):
            text = page.extract_text()
            print(f"\nProcessing page {page_num}")
            
            # Split text into sections for each locality
            localities = text.split('Locality No.')
            
            for loc in localities[1:]:  # Skip first empty split
                try:
                    # Initialize all variables
                    locality_no = None
                    latitude = None
                    longitude = None
                    unit = None
                    potential = None
                    lithology = None
                    comments = None
                    contact_info = None
                    
                    # Extract Locality Number
                    locality_match = re.search(r'^\s*(\d+)', loc)
                    if locality_match:
                        locality_no = locality_match.group(1)
                        print(f"\nProcessing Locality No. {locality_no}")
                    else:
                        print("Could not find Locality Number, skipping...")
                        continue
                    
                    # Extract Coordinates
                    # Look for the specific pattern: latitude followed by longitude
                    coords_pattern = r'(\d+°\s*\d+’\s*\d+(?:[.,]\d+)?’’\s*N)\s+(\d+°\s*\d+’\s*\d+(?:[.,]\d+)?’’\s*W)'
                    coords_match = re.search(coords_pattern, loc)
                    
                    if coords_match:
                        latitude = coords_match.group(1)
                        longitude = coords_match.group(2)

                    
                    # Extract Unit (looking for pattern between "Unit" and "Potential")
                    unit_pattern = r'Unit\s+(.*?)\s+Potential'
                    unit_match = re.search(unit_pattern, loc)
                    if unit_match:
                        unit = unit_match.group(1).strip()
                    
                    # Extract Potential
                    potential_pattern = r'Potential\s+(.*?)\s+Lithology'
                    potential_match = re.search(potential_pattern, loc)
                    if potential_match:
                        potential = potential_match.group(1).strip()
                    
                    # Extract Lithology
                    lithology_pattern = r'Lithology\s+(.*?)\s+Comments'
                    lithology_match = re.search(lithology_pattern, loc, re.DOTALL)
                    if lithology_match:
                        lithology = lithology_match.group(1).strip()
                    
                    # Extract Comments
                    comments_pattern = r'Comments\s+(.*?)\s+(?:Contact information|$)'
                    comments_match = re.search(comments_pattern, loc, re.DOTALL)
                    if comments_match:
                        comments = comments_match.group(1).strip()
                    
                    # Extract Contact Information
                    contact_pattern = r'Contact information\s+(.*?)(?=$)'
                    contact_match = re.search(contact_pattern, loc, re.DOTALL)
                    if contact_match:
                        contact_info = contact_match.group(1).strip()
                    
                    data = {
                        'Locality_No': locality_no,
                        'Latitude': latitude,
                        'Longitude': longitude,
                        'Unit': unit,
                        'Potential': potential,
                        'Lithology': lithology,
                        'Comments': comments,
                        'Contact_Information': contact_info
                    }
                    
                    # Print extracted data for debugging
                    print(f"Extracted data for Locality {locality_no}:")
                    print(f"Coordinates: {latitude} / {longitude}")
                    print(f"Unit: {unit}")
                    print(f"Potential: {potential}")
                    
                    extracted_data.append(data)
                    
                except Exception as e:
                    print(f"Error processing locality: {str(e)}")
                    continue
    
    if not extracted_data:
        raise ValueError("No data could be extracted from the PDF. Please check the format of your PDF file.")
    
    return extracted_data

def create_excel(data, output_path):
    """
    Create Excel file from extracted data.
    """
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Reorder columns for better readability
    column_order = [
        'Locality_No', 
        'Latitude', 
        'Longitude',
        'Unit', 
        'Potential',
        'Lithology',
        'Comments',
        'Contact_Information'
    ]
    
    # Ensure all columns exist
    for col in column_order:
        if col not in df.columns:
            df[col] = None
    
    df = df[column_order]
    
    # Format numeric columns
    try:
        df['Locality_No'] = pd.to_numeric(df['Locality_No'], errors='coerce')

    except Exception as e:
        print(f"Warning: Error formatting numeric columns: {str(e)}")
    
    # Set column widths and format
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Geological Data')
        worksheet = writer.sheets['Geological Data']
        
        # Adjust column widths
        cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        widths = [12, 12, 12, 20, 20, 25, 15, 50, 50, 20]
        
        for col, width in zip(cols, widths):
            worksheet.column_dimensions[col].width = width
    
    print(f"\nCreated Excel file with {len(df)} records")
    print("\nColumns in the Excel file:")
    print(df.columns.tolist())

def main():
    # Replace these paths with your actual file paths
    pdf_path = 'example.pdf'
    excel_path = 'output1.xlsx'
    
    try:
        print(f"Starting extraction from: {pdf_path}")
        data = extract_pdf_data(pdf_path)
        
        print(f"\nCreating Excel file at: {excel_path}")
        create_excel(data, excel_path)
        
        print("\nProcessing complete!")
        
    except FileNotFoundError:
        print(f"Error: Could not find the PDF file at {pdf_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("\nPlease ensure:")
        print("1. The PDF file exists and is readable")
        print("2. The PDF contains text (not scanned images)")
        print("3. The output directory is writable")

if __name__ == "__main__":
    main()