## Python PDF Merger Script

The provided Python script, **`Mergre_my_pdf.py`**, is a simple program that merges all PDF files in the current directory into a single PDF file. It utilizes the **PyPDF2** library to handle PDF operations. Below is a breakdown of how the script works:

### **How the Script Works**
1. **Imports Necessary Modules**
   - `os` for handling file operations.
   - `PyPDF2.PdfWriter` for merging PDF files.

2. **Identifies PDF Files**
   - The script scans the current directory (`os.listdir()`) and creates a list of all files that have a `.pdf` extension.

3. **Merges PDFs**
   - Using the `PdfWriter` class, it appends all the identified PDF files into a single PDF.

4. **User Input for Merged File Name**
   - The user is prompted to enter a name for the merged PDF file.
   - The merged file is saved with the given name.

5. **Option to View the Merged File**
   - After merging, the user is asked if they want to open the merged PDF.
   - If the user enters **'y'**, the script attempts to open the file using `os.startfile()`.
   - If the user enters **'n'**, the script exits with a friendly message.

### **Features**
✔ Automatically detects and merges all PDF files in the directory  
✔ User-friendly interaction for naming the merged file  
✔ Option to open the merged PDF after creation  
✔ Uses **PyPDF2**, a lightweight and efficient PDF-handling library   

This script is useful for **combining multiple PDFs** into one. Although, can be improved further to add more features an functionalities. 🚀
