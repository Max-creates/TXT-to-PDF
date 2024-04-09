from fpdf import FPDF
import glob
from pathlib import Path

# Create a list of filepaths
filepaths = glob.glob("files/*.txt")

# Create one PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Go through the filenames
for filepath in filepaths:
    # Add a page for each filename
    pdf.add_page()
    
    # Get the filename with the extension and convert it to title case
    filename = Path(filepath).stem.title()
    
    # Set the font
    pdf.set_font("Arial", "B", 16)
    
    # Add the filename
    pdf.cell(w=0, h=10, txt=filename, ln=1)
    
    # Read file and add text to pdf
    with open(filepath, "r") as file:
        text = file.read()
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(w=0, h=6, txt=text)

# Produce the PDF
pdf.output("output.pdf")
