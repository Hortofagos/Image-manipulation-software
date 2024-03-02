from PIL import Image, ImageEnhance
import os

def apply_warm_filter(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            # Applying a warm filter using ImageEnhance.Color
            enhancer = ImageEnhance.Color(img)
            img_warm = enhancer.enhance(1.7)  # You can adjust the enhancement factor

            # Save the result
            img_warm.save(output_path)
            print(f"Filtered image saved to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        input_file = os.path.join(folder_path, filename)

        # Check if the file is an image (you can add more image formats if needed)
        if input_file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            output_file = os.path.join(folder_path, f"output_warm_{filename}")
            apply_warm_filter(input_file, output_file)
        else:
            print(f"Skipping unsupported file: {filename}")

def main():
    folder_path = '/home/horto/Desktop/tests'  # Replace with the path to your folder containing images
    process_folder(folder_path)

if __name__ == "__main__":
    main()
