from PIL import Image, ImageFilter

# Open the image file
img = Image.open('./Pokedex/pikachu.jpg')

# Print the image object and its properties
print(img)                       # Display the image object
print(img.format)               # Print the format of the image (e.g., JPEG, PNG)
print(img.size)                 # Print the dimensions of the image (width, height)
print(img.mode)                 # Print the color mode of the image (e.g., RGB, L)

# Apply a blur filter to the image and save the result
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("./Pokedex/blur.png", "png")

# Apply a smooth filter to the image and save the result
filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save("./Pokedex/smooth.png", "png")

# Apply a sharpen filter to the image and save the result
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("./Pokedex/sharpen.png", "png")

# Convert the image to greyscale (black and white) and save the result
filtered_img = img.convert('L')  # 'L' mode represents greyscale
filtered_img.save("./Pokedex/grey.png", "png")

# Uncomment the line below to open the image in the default image viewer
# filtered_img.show()  # Opens the image in the default image viewer

# Rotate the image by 45 degrees and save the result
rotated_img = img.rotate(45)
rotated_img.save("./Pokedex/rotated.png", "png")

# Resize the image to 300x300 pixels and save the result
resized_img = img.resize((300, 300))  # Note: This may alter the aspect ratio
resized_img.save("./Pokedex/resized.png", "png")

# Define a box for cropping the image (left, upper, right, lower)
box = (100, 100, 400, 400)
cropped_img = img.crop(box)  # Crop the image using the defined box
cropped_img.save("./Pokedex/cropped.png", "png")

# Create a thumbnail of the image with a maximum size of 100x50 pixels
img.thumbnail((100, 50))  # Maintains the aspect ratio and does not exceed the specified size
img.save("./Pokedex/thumbnail.png", "png")  # Save the thumbnail image
