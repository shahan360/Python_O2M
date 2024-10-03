# Import necessary libraries
import PyPDF2  # Library for working with PDF files
import sys     # Library for handling command-line arguments

# Retrieve all command-line arguments except the first one
# sys.argv[0] is the script name, sys.argv[1:] contains the remaining arguments (PDF file paths)
inputs = sys.argv[1:]

def pdf_merger(pdf_list):
    """
    Merges multiple PDF files into a single PDF file.

    Parameters:
    pdf_list (list): A list of PDF file paths to be merged.

    The function uses PyPDF2's PdfMerger class to merge the PDFs and writes 
    the merged output to './PDF/merged.pdf'.
    """
    # Create an instance of PdfMerger to handle PDF merging
    merger = PyPDF2.PdfMerger()  # Changed from PdfFileMerger to PdfMerger

    # Loop through the list of PDFs and append them one by one
    for pdf in pdf_list:
        merger.append(pdf)
    
    # Write the merged PDF to the specified output file path
    merger.write('/Users/shahan/Coding_Projects/Python_O2M/Scripting/PDF/merged.pdf')
    merger.close()  # Close the merger to finalize the output file

# Call the pdf_merger function, passing the list of PDF files as arguments
pdf_merger(inputs)
