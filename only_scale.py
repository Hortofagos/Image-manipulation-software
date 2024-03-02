import cv2
import os
import random
import string


# Function to generate a random string for the new filename
def generate_random_filename(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


# Path to the folder containing images to be scrambled
input_folder = '/home/horto/Desktop/tests'  # Replace with the path to your input image folder

# Path to the folder where resized and scrambled images will be saved
output_folder = '/home/horto/Desktop/tests1'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate over all files in the input folder
for x in range(10):
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(input_folder, filename)
            scrambled_image = cv2.imread(image_path)

            # - Scaling the scrambled image
            scale_factor = random.uniform(0.8, 1.2)  # Adjust this factor as needed
            new_width = int(scrambled_image.shape[1] * scale_factor)
            new_height = int(scrambled_image.shape[0] * scale_factor)
            scaled_image = cv2.resize(scrambled_image, (new_width, new_height))

            # Generate a random filename
            new_filename = generate_random_filename() + os.path.splitext(filename)[1]
            output_path = os.path.join(output_folder, new_filename)

            # Save the scrambled and scaled image to the output folder
            cv2.imwrite(output_path, scaled_image)

            print(f'Scrambled and scaled image saved: {output_path}')
