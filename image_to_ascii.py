from PIL import Image, ImageOps,ImageFont, ImageDraw
import numpy as np
from tkinter.filedialog import askopenfilename


densities = "N@#W$9876543210?!abc;:+=-,-"
image_path = askopenfilename()
image = Image.open(image_path)
image_size = image.size


def create_text_file(image):
    image_array = np.asarray(image)
    file_handler = open("image.txt", 'w')
    for row in image_array:
        for _ in row:
            num = int(_)
            character = densities[num//len(densities)]
            file_handler.write(character)
        file_handler.write("\n")
    file_handler.close()

    return "image.txt"


def create_image(file_path):
    fileHandler = open(file_path, 'r')    
    lines = tuple(map( lambda line : line.rstrip(), fileHandler.readlines() ))
    font = ImageFont.load_default()

    line_height = font.getsize( max(lines, key = lambda line : font.getsize(line)[1]) )[1]

    width = font.getsize( max(lines, key = lambda line : font.getsize(line)[0]) )[0]
    height = line_height * len(lines)
    
    image = Image.new("L", (width, height))
    image_draw = ImageDraw.Draw(image)

    for index, line in enumerate(lines):
        line_y = index*line_height    
        image_draw.text((0, line_y), line, font=font, fill=255)
    
    image = image.resize(image_size)
    return image

gray_scale_image = ImageOps.grayscale(image)
file_path = create_text_file(gray_scale_image)
ascii_image = create_image(file_path)
ascii_image.save('ascii_image.png')
