from PIL import Image, ImageEnhance
import os
import subprocess
import piexif
from datetime import datetime, timedelta
import random

def change_color_scheme(image_path, output_path):
    def shift_hue(image, hue_shift_factor):
        rgb_image = image.convert('RGB')

        # Create a new image to store the shifted hue
        shifted_image = Image.new('RGB', image.size)

        for y in range(image.height):
            for x in range(image.width):
                r, g, b = rgb_image.getpixel((x, y))

                # Convert RGB to HSV
                max_value = max(r, g, b)
                min_value = min(r, g, b)
                delta = max_value - min_value

                value = max_value / 255.0
                saturation = 0 if max_value == 0 else delta / max_value

                if delta == 0:
                    hue = 0  # undefined, but we'll set it to 0
                elif max_value == r:
                    hue = ((g - b) / delta) % 6
                elif max_value == g:
                    hue = (b - r) / delta + 2
                else:
                    hue = (r - g) / delta + 4

                # Adjust hue
                hue = (hue + hue_shift_factor) % 6

                # Convert HSV back to RGB
                c = value * saturation
                x1 = c * (1 - abs(hue % 2 - 1)) + 1e-6
                m = value - c

                if 0 <= hue < 1:
                    rgb_shifted = (c, x1, 0)
                elif 1 <= hue < 2:
                    rgb_shifted = (x1, c, 0)
                elif 2 <= hue < 3:
                    rgb_shifted = (0, c, x1)
                elif 3 <= hue < 4:
                    rgb_shifted = (0, x1, c)
                elif 4 <= hue < 5:
                    rgb_shifted = (x1, 0, c)
                else:
                    rgb_shifted = (c, 0, x1)

                r_shifted = int((rgb_shifted[0] + m) * 255)
                g_shifted = int((rgb_shifted[1] + m) * 255)
                b_shifted = int((rgb_shifted[2] + m) * 255)

                # Ensure RGB values are integers
                r_shifted = int(round(r_shifted))
                g_shifted = int(round(g_shifted))
                b_shifted = int(round(b_shifted))
                shifted_image.putpixel((round(x), y), (r_shifted, g_shifted, b_shifted))

        return shifted_image

    imagee = Image.open(image_path)

    shifted_image_out = shift_hue(imagee, 0.02)
    exif_data = imagee.info.get('exif', b'')
    if exif_data:
        exif_dict = piexif.load(exif_data)
    else:
        exif_dict = {"0th": {}, "Exif": {}}

    current_time = datetime.now()
    time_difference = timedelta(hours=-5, minutes=-random.randrange(58, 60))
    # Calculate the new timestamp with the offset
    new_timestamp = current_time + time_difference
    # Format the timestamp as a string
    timestamp = new_timestamp.strftime("%Y:%m:%d %H:%M:%S")
    exif_dict["Exif"][36867] = timestamp

    # Convert the modified Exif data back to bytes
    exif_bytes = piexif.dump(exif_dict)

    # Save the image with the modified timestamp
    shifted_image_out.save(output_path, exif=exif_bytes)

    print('Color scheme changed successfully for', image_path)

if __name__ == "__main__":
    input_folder = '/home/horto/Desktop/tests'  # Replace with the actual folder path
    output_folder = '/home/horto/Desktop/tests1'  # Output folder to save processed images

    # Example enhancement factor (1.0 for no change, <1.0 for desaturation, >1.0 for saturation)

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):  # Check if it's an image file
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)

            # Change color scheme
            change_color_scheme(input_image_path, output_image_path)
