import os
import sys
from PIL import Image, ImageOps

# Check for correct number of command-line arguments
if len(sys.argv) != 3:
    print("Use: python shirt.py input_image output_image")
    sys.exit(1)

# Check for valid file extensions
input_ext = os.path.splitext(sys.argv[1])[1].lower()
output_ext = os.path.splitext(sys.argv[2])[1].lower()
if input_ext not in ['.jpg', '.jpeg', '.png'] or output_ext not in ['.jpg', '.jpeg', '.png']:
    print("Error: Input and output files must be JPEG or PNG")
    sys.exit(1)

# Check for same input and output file extensions
if input_ext != output_ext:
    print("Error: Input and output files must have the same extension")
    sys.exit(1)

# Check if input file exists
if not os.path.exists(sys.argv[1]):
    print("Error: Input file does not exist")
    sys.exit(1)

# Load input and shirt images
input_image = Image.open(sys.argv[1])
shirt_image = Image.open("shirt.png")

# Resize and crop input to same size as shirt
resized_input_image = ImageOps.fit(input_image, shirt_image.size)

# Overlay shirt on input
output_image = resized_input_image.copy()
output_image.paste(shirt_image, (0, 0), shirt_image)

# Save output image
output_image.save(sys.argv[2])
