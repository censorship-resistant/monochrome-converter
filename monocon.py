import cairosvg
from PIL import Image
import os

# Define the directory containing the icons
input_dir = '/path/to/your/icontheme'
output_dir = '/your/output/path'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Loop over all files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.svg'):
        svg_path = os.path.join(input_dir, filename)
        png_path = os.path.join(output_dir, filename.replace('.svg', '.png'))

        # Convert SVG to PNG
        cairosvg.svg2png(url=svg_path, write_to=png_path)

        # Open the PNG file
        with Image.open(png_path) as img:
            # Convert image to grayscale and keep alpha channel
            grayscale_img = img.convert('LA')

            # Resize the image to 128x128
            resized_img = grayscale_img.resize((128, 128), Image.Resampling.LANCZOS)

            # Save the resized grayscale image
            resized_img.save(png_path)

print("Conversion complete!")
