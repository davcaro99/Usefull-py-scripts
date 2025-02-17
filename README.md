# Useful Py Scripts

A collection of Python scripts designed to simplify common tasks related to **coordinate conversion, PDF metadata extraction, and geological data processing**.

## 📜 Scripts Overview

### 1️⃣ Convert DMS to DD (`dms_to_dd.py`)
- Converts **DMS coordinates** (Degrees, Minutes, Seconds) in a CSV file to **Decimal Degrees (DD)**.
- Input: CSV file with `Latitude` and `Longitude` columns.
- Output: CSV file with converted coordinates in DD format.

### 2️⃣ Extract PDF Metadata (`pdf_metadata_extractor.py`)
- Extracts metadata from all **PDF files** in a folder and compiles it into a CSV file.
- Designed for organizing **PDF book collections** by retrieving key details.
- Input: Folder containing PDFs.
- Output: CSV file with extracted metadata.

### 3️⃣ Extract Georeferenced Data from PDFs (`geological_data_extractor.py`)
- Parses a **PDF list of geological (or georeferenced) localities**, extracting relevant data.
- Extracts **coordinates, names, measurements, comments, and images**.
- Output: CSV file that can be converted into a **KMZ file** for mapping.
- Users can **customize** the script based on the PDF structure.

## 🚀 How to Use
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/Useful-Py-Scripts.git
   cd Useful-Py-Scripts
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the scripts:
   ```sh
   python dms_to_dd.py input.csv output.csv
   ```
   ```sh
   python pdf_metadata_extractor.py input_folder output.csv
   ```
   ```sh
   python geological_data_extractor.py input.pdf output.csv
   ```
## Author
- **David Caro**  
- 📧 [decaroc@unal.edu.co](mailto:decaroc@unal.edu.co)