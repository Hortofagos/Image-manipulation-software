from PIL import Image
import os

# Function to adjust the size while preserving aspect ratio
def adjust_size_with_aspect_ratio(image, target_ratio):
    width, height = image.size
    current_ratio = width / height

    if current_ratio > target_ratio:
        new_width = int(height * target_ratio)
        new_height = height
    else:
        new_width = width
        new_height = int(width / target_ratio)

    return image.resize((new_width, new_height), Image.BILINEAR)

# Path to the folder containing images to be adjusted
input_folder = '/home/horto/Desktop/tests1'

# Path to the folder where adjusted images will be saved
output_folder = '/home/horto/Desktop/9_16'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Specify the target aspect ratio (9:16)
target_ratio = 9 / 16

# Iterate over all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(input_folder, filename)
        original_image = Image.open(image_path)

        # Adjust the size while preserving the aspect ratio
        adjusted_image = adjust_size_with_aspect_ratio(original_image, target_ratio)

        # Generate a new filename with adjusted image size
        new_filename = f"adjusted_{filename}"
        output_path = os.path.join(output_folder, new_filename)

        # Save the adjusted image to the output folder
        adjusted_image.save(output_path)

        print(f'Adjusted image saved: {output_path}')

        adjusted_image.close()
