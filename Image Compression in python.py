import PIL
from PIL import Image
import os

needed_width = 1080

existing_dir = "C:/Users/DELL/Downloads/New"
new_dir = "C:/Users/DELL/Downloads/z"

# Commands


def compress_image(exist_pic, new_pic, width):
    img = Image.open(exist_pic)
    w_percent = (width/float(img.size[0]))
    h_size = int((float(img.size[1])*float(w_percent)))
    img = img.resize((width, h_size), PIL.Image.ANTIALIAS)
    print(new_pic)
    img.save(new_pic)


def multiple_compress(exist_dir, new_p_dir, width):
    pics = os.listdir(exist_dir)
    print(pics)

    for pic in pics:
        exist_dir = existing_dir + "/" + pic
        new_p_dir = new_dir + "/" + pic
        compress_image(exist_dir, new_p_dir, width)


multiple_compress(existing_dir, new_dir, needed_width)