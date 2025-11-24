import os
from PIL import Image

INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"

NEW_SIZE = (800, 600)  

def resize_images():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    for filename in os.listdir(INPUT_FOLDER):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            img_path = os.path.join(INPUT_FOLDER, filename)
            img = Image.open(img_path)

            original_size = img.size

            img_resized = img.resize(NEW_SIZE)

            resized_size = img_resized.size

            output_path = os.path.join(OUTPUT_FOLDER, filename)
            img_resized.save(output_path)

            print(f"Processed: {filename}")
            print(f" Original Size: {original_size}")
            print(f" Resized Size: {resized_size}\n")

    print("All images have been resized successfully!")

if __name__ == "__main__":
    resize_images()
