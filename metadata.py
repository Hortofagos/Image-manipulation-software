from PIL import Image
import os
import piexif
import datetime

def modify_exif_with_timestamp(image_path, output_path, make, model):
    try:
        # Open the image using Pillow
        img = Image.open(image_path)

        # Get the existing Exif data or create a new one if it doesn't exist
        exif_data = img.info.get('exif', b'')

        if exif_data:
            exif_dict = piexif.load(exif_data)
        else:
            exif_dict = {"0th": {}, "Exif": {}}

        # Modify the Exif data with the specified attributes
        exif_dict["0th"][271] = make  # 'Make' Exif tag
        exif_dict["0th"][272] = model  # 'Model' Exif tag

        # Convert the modified Exif data back to bytes
        exif_bytes = piexif.dump(exif_dict)

        # Save the image with the modified metadata
        img.save(output_path, exif=exif_bytes)

        print('Metadata modified with timestamp and saved to:', output_path)
    except Exception as e:
        print('Error:', str(e))

if __name__ == '__main__':
    # Specify the input and output folders
    input_folder = '/home/horto/Desktop/tests'
    output_folder = '/home/horto/Desktop/tests1'

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        image_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Specify camera attributes
        make = 'Samsung'
        model = 'SM-A530F'

        # Call the function to modify Exif data and add a timestamp to the metadata
        modify_exif_with_timestamp(image_path, output_path, make, model)
