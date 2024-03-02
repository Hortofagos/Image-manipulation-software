import os
import subprocess
import shutil

def convert_heic_to_jpeg(input_path, output_path):
    subprocess.run(["heif-convert", input_path, output_path])

def convert_heic_files_to_jpeg(input_folder, output_folder):
    for root, _, files in os.walk(input_folder):
        for filename in files:
            input_path = os.path.join(root, filename)

            # Check if the file is a HEIC image
            if filename.lower().endswith(".heic"):
                output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")
                convert_heic_to_jpeg(input_path, output_path)
                print(f"Converted {input_path} to {output_path}")
            else:
                # File is not a HEIC image, so copy it to "tests1"
                output_path = os.path.join(output_folder, filename)
                shutil.copy(input_path, output_path)
                print(f"Copied {input_path} to {output_path}")

if __name__ == "__main__":
    input_folder = '/home/horto/Desktop/tests'
    output_folder = '/home/horto/Desktop/tests1'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    convert_heic_files_to_jpeg(input_folder, output_folder)
