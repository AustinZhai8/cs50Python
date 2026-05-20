import sys
from PIL import Image, ImageOps

if len(sys.argv) != 3:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

valid_extensions = {'.jpg', '.jpeg', '.png'}

input_ext = None
output_ext = None

for ext in valid_extensions:
    if input_file.lower().endswith(ext):
        input_ext = ext
        break

for ext in valid_extensions:
    if output_file.lower().endswith(ext):
        output_ext = ext
        break

if input_ext is None:
    sys.exit("Invalid input")


if output_ext is None:
    sys.exit("Invalid output")

if input_ext != output_ext:
    sys.exit("Input and output have different extensions")

try:
    with open(input_file, 'r'):
        pass
except FileNotFoundError:
    sys.exit("Input does not exist")

input_image = Image.open(input_file)

shirt_image = Image.open("shirt.png")

resized_input = ImageOps.fit(input_image, shirt_image.size, method=Image.Resampling.LANCZOS)

resized_input.paste(shirt_image, (0, 0), shirt_image)

resized_input.save(output_file)
