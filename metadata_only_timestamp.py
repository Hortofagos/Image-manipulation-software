import random

from PIL import Image
import os
import piexif
from datetime import datetime, timedelta


def modify_exif_timestamp(image_path, output_path):
        # Open the image using Pillow
        img = Image.open(image_path)

        # Get the existing Exif data or create a new one if it doesn't exist
        exif_data = img.info.get('exif', b'')

        if exif_data:
            exif_dict = piexif.load(exif_data)
        else:
            exif_dict = {"0th": {}, "Exif": {}}

        current_time = datetime.now()
        time_difference = timedelta(hours=-6, minutes=-random.randrange(58, 60))
        # Calculate the new timestamp with the offset
        new_timestamp = current_time + time_difference
        # Format the timestamp as a string
        timestamp = new_timestamp.strftime("%Y:%m:%d %H:%M:%S")
        exif_dict["Exif"][36867] = timestamp

        # Convert the modified Exif data back to bytes
        exif_bytes = piexif.dump(exif_dict)

        # Save the image with the modified timestamp
        img.save(output_path, exif=exif_bytes)

        print('Timestamp modified and saved to:', output_path)

        return "Success"


# Specify the input and output folders
input_folder = '/home/horto/Desktop/tests'
output_folder = '/home/horto/Desktop/tests1'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    image_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)

    # Call the function to modify the timestamp in the metadata
    result = modify_exif_timestamp(image_path, output_path)
    print(result)  # Print the result of the modification
