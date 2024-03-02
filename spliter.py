from PIL import Image
import os

def split_image_into_3_squares(input_image_path, output_folder):
    # Open the input image
    image = Image.open(input_image_path)

    # Get the dimensions of the input image
    width, height = image.size

    # Calculate the dimensions of each square
    square_width = width // 3
    square_height = height

    for i in range(3):
        # Calculate the coordinates for each square
        left = i * square_width
        upper = 0
        right = (i + 1) * square_width
        lower = square_height

        # Crop and save the square
        square = image.crop((left, upper, right, lower))
        square.save(os.path.join(output_folder, f"square_{i + 1}.png"))

def split_images_in_folder(input_folder, output_folder):
    # Iterate over files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp")):  # Add more file extensions if needed
            input_image_path = os.path.join(input_folder, filename)
            split_image_into_3_squares(input_image_path, output_folder)
            print(f"Split and saved squares for {filename}")

if __name__ == "__main__":
    input_folder = "/home/horto/Desktop/spit"  # Replace with the path to your input folder
    output_folder = "/home/horto/Desktop/spit_out"  # Replace with the path to your output folder

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    split_images_in_folder(input_folder, output_folder)
