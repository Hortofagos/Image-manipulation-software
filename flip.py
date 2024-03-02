import os
from PIL import Image


# Function to horizontally mirror (flip) an image while preserving metadata
def mirror_image_horizontally(input_path, output_path):
    original_image = Image.open(input_path)

    # Check if the image has Exif data
    exif_dict = original_image.info.get('exif')

    # Horizontally mirror (flip) the image
    mirrored_image = original_image.transpose(Image.FLIP_LEFT_RIGHT)

    # Save the horizontally mirrored image with the original Exif data
    mirrored_image.save(output_path, format=original_image.format, exif=exif_dict)


# Input and output directories
input_dir = '/home/horto/Desktop/tests'  # Replace with the path to your input image folder
output_dir = '/home/horto/Desktop/tests1'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate over the files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # Process only image files
        input_path = os.path.join(input_dir, filename)

        # Generate the output path for the horizontally mirrored image
        output_path = os.path.join(output_dir, 'mirrored_' + filename)

        # Horizontally mirror the image while preserving metadata
        mirror_image_horizontally(input_path, output_path)

        print('Horizontally mirrored image saved at:', output_path)
