import os
import piexif
from PIL import Image

def remove_location_metadata(image_path):
    try:
        # Open the image
        img = Image.open(image_path)

        # Check if the image has Exif data
        if 'exif' in img.info:
            exif_dict = piexif.load(img.info['exif'])

            # Remove all GPS-related tags
            if piexif.GPSIFD in exif_dict:
                exif_dict.pop(piexif.GPSIFD, None)

                # Save the modified Exif data back to the image
                exif_bytes = piexif.dump(exif_dict)
                img.save(image_path, exif=exif_bytes)

                print(f"Location metadata removed from {image_path}")
            else:
                print(f"No GPS metadata found in {image_path}")
        else:
            print(f"No Exif data found in {image_path}")

    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def remove_location_metadata_in_folder(folder_path):
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(folder_path, filename)
            remove_location_metadata(image_path)

if __name__ == "__main__":
    folder_path = "/home/horto/Desktop/tests"
    remove_location_metadata_in_folder(folder_path)
