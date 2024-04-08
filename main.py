from fpdf import FPDF
import glob
from pathlib import Path

# Create a list of filepaths
filepaths = glob.glob("files/*.txt")
# Create a list of filenames without the extension and paths
filenames = [Path(filepath).stem for filepath in filepaths]

# Create one PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Go through the filenames
for filename in filenames:
    # Add a page for each filename
    pdf.add_page()
    # Set the font
    pdf.set_font("Arial", "B", 16)
    # Write the filename in the top-left corner and capitalize the first letter
    # using the .title() method
    pdf.cell(w=0, h=10, txt=filename.title(), ln=1, align="L")

# Produce the PDF
pdf.output("output.pdf")
