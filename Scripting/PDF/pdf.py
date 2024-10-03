# Import the PyPDF2 module to work with PDF files
import PyPDF2

# Open the PDF file in read-binary mode ('rb')
with open('/Users/shahan/Coding_Projects/Python_O2M/Scripting/PDF/dummy.pdf', 'rb') as file:
    # Create a PdfReader object to read the PDF file
    reader = PyPDF2.PdfReader(file)

    # Print the file object and the reader object for debugging purposes
    print(file)  # Displays the file object
    print(reader)  # Displays the PdfReader object

    # Print the total number of pages in the PDF
    print(len(reader.pages))

    # Retrieve the first page (index 0) of the PDF
    page = reader.pages[0]

    # Rotate the page 90 degrees clockwise
    page.rotate(90)

    # Create a PdfWriter object to write to a new PDF file
    writer = PyPDF2.PdfWriter()

    # Add the rotated page to the writer object
    writer.add_page(page)

    # Open a new PDF file in write-binary mode ('wb') to save the rotated page
    with open('/Users/shahan/Coding_Projects/Python_O2M/Scripting/PDF/rotated.pdf', 'wb') as new_file:
        # Write the modified PDF content to the new file
        writer.write(new_file)
