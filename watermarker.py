import os
from PIL import Image, ImageDraw, ImageFont
import string
import random

# Define the watermark text and font
watermark_text = "@cute_carla_04"
font = ImageFont.truetype("Purisa-Bold.ttf", 56)  # You may need to specify the path to a TrueType font file.

# Define the text color and opacity
text_color = (255, 255, 255)  # White text color
opacity = 100

# Input and output folder paths
input_folder = "/home/horto/Desktop/watermark"
output_folder = "/home/horto/Desktop/watermark1"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def generate_random_filename(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# List all image files in the input folder
for x in range(10):
    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".png")):
            # Open the image
            image = Image.open(os.path.join(input_folder, filename))

            # Create a drawing context
            draw = ImageDraw.Draw(image)

            # Determine the position for the watermark
            position = (random.randrange(10, 400), 10)

            # Add the watermark text to the image
            draw.text(position, watermark_text, fill=text_color, font=font, align="center")

            # Save the image with the watermark to the output folder
            new_filename = generate_random_filename() + os.path.splitext(filename)[1]
            output_path = os.path.join(output_folder, new_filename)

            image.save(output_path)

            print(f"Watermark added to {filename} and saved as {output_path}")
