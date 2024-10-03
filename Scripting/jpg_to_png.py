# Import necessary libraries
from PIL import Image  # For image processing
import sys  # For handling command-line arguments
import os   # For interacting with the operating system (e.g., checking file paths)

# Get the input and output directory paths from the command-line arguments
img_path = sys.argv[1]  # Path to the directory containing input images
output_path = sys.argv[2]  # Path to the directory where converted images will be saved

# Check if the output directory exists, and if not, create it
if not os.path.exists(output_path):
    os.makedirs(output_path)  # Create the output directory if it doesn't exist

# Loop through each file in the input directory
for filename in os.listdir(img_path):
    # Open the image using the file path
    img = Image.open(f'{img_path}/{filename}')
    
    # Extract the filename without the extension using os.path.splitext
    # This avoids hard-coding specific extensions (like ".jpg")
    new_file = os.path.splitext(filename)[0]
    
    # Save the image in PNG format in the output directory
    img.save(f"{output_path}/{new_file}.png", "png")
