import os
from PIL import Image

input_dir = "input_images"
output_dir = "output_images"

if output_dir not in os.listdir():
    os.mkdir(output_dir)

files = os.listdir(input_dir)
image_files = []

for el in files:
    splt = el.split(".")
    ext = splt.pop()
    if ext in "jpg jpeg png bmp JPG JPEG PNG BMP":
        image = Image.open(input_dir + "/" + el)
        x, y = image.size
        if x > y :
            new_size = x
            x_offset = 0
            y_offset = int((x-y)/2)
        elif y > x:
            new_size = y
            x_offset = int((y-x) / 2)
            y_offset = 0

        background_color = "white"  #white, black, blue, red, ...
        new_image = Image.new("RGBA", (new_size, new_size), background_color)
        new_image.paste(image, (x_offset, y_offset))

        outfile_name = ".".join(splt) + ".png"
        new_image.save(output_dir + "/" + outfile_name)
