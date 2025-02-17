# Useful Py Scripts

A collection of Python scripts designed to simplify common tasks related to **coordinate conversion, PDF metadata extraction, and geological data processing**.

## 📜 Scripts Overview

### 1️⃣ Convert DMS to DD (`convertcoordinates.py.py`)
- Converts **DMS coordinates** (Degrees, Minutes, Seconds) in a CSV file to **Decimal Degrees (DD)**.
- Input: CSV file with `Latitude` and `Longitude` columns.
- Output: CSV file with converted coordinates in DD format.

### 2️⃣ Extract PDF Metadata (`pdf_metadata_extractor.py`)
- Extracts metadata from all **PDF files** in a folder and compiles it into a CSV file.
- Designed for organizing **PDF book collections** by retrieving key details.
- Input: Folder containing PDFs.
- Output: CSV file with extracted metadata.

### 3️⃣ Extract Georeferenced Data from PDFs (`pdfcoordpoints.py.py`)
- Parses a **PDF list of geological (or georeferenced) localities**, extracting relevant data.
- Extracts **coordinates, names, measurements, comments, and images**.
- Output: CSV file that can be converted into a **KMZ file** for mapping.
- Users can **customize** the script based on the PDF structure.

## Author
- **David Caro**  
- 📧 [decaroc@unal.edu.co](mailto:decaroc@unal.edu.co)