import os
import random
from PIL import Image, ImageEnhance

# Function to generate a random value for color adjustment
def random_color_adjustment():
    return random.uniform(0.8, 1.2)

# Path to the folder containing images to be modified
input_dir = '/home/horto/Desktop/tests'  # Replace with the path to your input image folder

# Path to the folder where modified images will be saved
output_dir = '/home/horto/Desktop/tests1'

# Create the output folder if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate over all files in the input folder
for filename in os.listdir(input_dir):
    image_path = os.path.join(input_dir, filename)
    original_image = Image.open(image_path)

    # Create a copy of the original image
    modified_image = original_image.copy()

    # Adjust the color using ImageEnhance
    enhancer = ImageEnhance.Color(modified_image)
    modified_image = enhancer.enhance(random_color_adjustment())

    # Generate the output path for the modified image
    output_path = os.path.join(output_dir, filename)

    # Get the EXIF data as bytes
    exif_bytes = original_image.info.get('exif')

    # Save the modified image without altering metadata
    if exif_bytes:
        modified_image.save(output_path, exif=exif_bytes)
    else:
        modified_image.save(output_path)

    print(f'Modified image saved without altering metadata: {output_path}')
