# Import the PyPDF2 library to work with PDF files
import PyPDF2

# Open the main PDF file (template) in read-binary mode
template = PyPDF2.PdfReader(open('/Users/shahan/Coding_Projects/Python_O2M/Scripting/PDF/super.pdf', 'rb'))

# Open the watermark PDF file in read-binary mode
watermark = PyPDF2.PdfReader(open('/Users/shahan/Coding_Projects/Python_O2M/Scripting/PDF/wtr.pdf', 'rb'))

# Create a PdfWriter object to store the output PDF with watermark
output = PyPDF2.PdfWriter()

# Loop through all the pages of the template PDF
for i in range(len(template.pages)):
    # Get each page of the template PDF
    page = template.pages[i]
    
    # Merge the first page of the watermark PDF with the current template page
    page.merge_page(watermark.pages[0])
    
    # Add the merged page to the output PDF
    output.add_page(page)

# Save the output watermarked PDF to a new file in write-binary mode
with open('/Users/shahan/Coding_Projects/Python_O2M/Scripting/PDF/watermarked_output.pdf', 'wb') as file:
    # Write the final output PDF to the file
    output.write(file)
