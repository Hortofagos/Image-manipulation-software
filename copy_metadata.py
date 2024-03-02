from PIL import Image
import piexif

def copy_metadata(source_path, destination_path):
    #try:
        # Open the source image
        source_image = Image.open(source_path)

        # Open the destination image (create a copy)
        destination_image = Image.open(destination_path)

        # Check if the source image has EXIF data
        if 'exif' in source_image.info:
            # Copy EXIF metadata from the source image to the destination image using piexif
            source_exif = piexif.load(source_image.info['exif'])

            # Check if the destination image has EXIF data
            destination_exif = piexif.load(destination_image.info.get('exif', b''))

            # Update the destination EXIF data with the source EXIF data
            destination_exif.update(source_exif)

            # Save the destination image with the copied metadata
            destination_image.save(destination_path, format='JPEG', quality='keep', exif=piexif.dump(destination_exif))

            print(f"Metadata copied from {source_path} to {destination_path}")
        else:
            # If the source image has no EXIF data, simply save the destination image
            destination_image.save(destination_path, format='JPEG', quality='keep')
            print(f"No metadata to copy. Saving destination image as is.")
    #except Exception as e:
        #print(f"Error: {e}")

# Example usage:
source_file_path = '/home/horto/Desktop/face_in/IMG_3322.JPG'
destination_file_path = '/home/horto/Desktop/face_in/IMG_3322_cloaked.jpeg'

copy_metadata(source_file_path, destination_file_path)
