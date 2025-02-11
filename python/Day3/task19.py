#Writing Binary Data from an Image

with open(r"C:\Users\harsh\Downloads\20231106154433_IMG_0615.JPG", 'rb') as img_file:  # Read the image as binary
    img_data = img_file.read()

with open(r"C:\Users\harsh\Downloads\n p.jpg", 'wb') as new_img_file:  # Write binary data
    new_img_file.write(img_data)

print("Image copied successfully.")


# The rb mode reads an image file in binary format.
# The wb mode writes the binary data to a new image file.