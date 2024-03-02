import cv2
from PIL import Image, ImageDraw


def apply_face_filter(input_image_path, output_image_path, filter_image_path):
    # Load the image
    image = cv2.imread(input_image_path)

    # Load the pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Load the filter image
    filter_img = Image.open(filter_image_path)

    # Convert OpenCV image to Pillow image
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)

    # Apply the filter to each detected face
    for (x, y, w, h) in faces:
        # Resize the filter to fit the face
        filter_resized = filter_img.resize((w, h))

        # Paste the filter onto the face
        pil_image.paste(filter_resized, (x, y), filter_resized)

    # Save the output image
    pil_image.save(output_image_path)


if __name__ == "__main__":
    # Provide the paths to the input image, output image, and filter image
    input_image_path = "path/to/input/image.jpg"
    output_image_path = "path/to/output/image_with_filter.jpg"
    filter_image_path = "path/to/filter/image.png"

    # Apply the face filter
    apply_face_filter(input_image_path, output_image_path, filter_image_path)
