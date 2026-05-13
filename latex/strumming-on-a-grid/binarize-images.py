import os
from PIL import Image

def binarize_images():
    # Loop through every file in the current directory
    for filename in os.listdir('.'):
        if filename.lower().endswith('.png'):
            try:
                # Open the image and convert to grayscale ('L' mode)
                img = Image.open(filename).convert('L')
                
                # Apply a threshold: 0 if below 128 (black), 255 if above (white)
                # This ensures colors closer to black become black, and vice versa
                img = img.point(lambda x: 0 if x < 128 else 255, '1')
                
                # Save the result, overwriting the original or changing the name
                img.save(filename)
                print(f"Processed: {filename}")
            except Exception as e:
                print(f"Could not process {filename}: {e}")

if __name__ == "__main__":
    binarize_images()

