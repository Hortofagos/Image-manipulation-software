import os
import cv2
image_path = os.path.join(input_folder, filename)

# Specify output path for the modified image
output_folder = '/home/horto/Desktop/tests1'
output_path = os.path.join(output_folder, filename)
# Path to the folder containing images to be resized
input_folder = '/home/horto/Desktop/tests'  # Replace with the path to your input image folder

# Path to the folder where resized images will be saved
output_folder = '/home/horto/Desktop/tests1'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate over all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(input_folder, filename)
        original_image = cv2.imread(image_path)

        # Check if the image is valid
        if original_image is not None:
            # Resize the image to half its original dimensions
            resized_image = cv2.resize(original_image, (0, 0), fx=0.5, fy=0.5)

            # Save the resized image to the output folder
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, resized_image)

            print(f'Resized image saved: {output_path}')
        else:
            print(f'Invalid image: {image_path}')
