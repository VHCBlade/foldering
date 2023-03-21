from PIL import Image
import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
tifToJpgConfig = config['tif-to-jpg']


input_dir = tifToJpgConfig["input"]
output_dir = tifToJpgConfig["output"]


def tif_to_jpg(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if not (filename.endswith('.tif') or filename.endswith('.tiff')):
            continue
        print("Converting " + filename + "...")
        img = Image.open(os.path.join(input_folder, filename))

        rgb_img = img.convert('RGB')

        jpg_filename = os.path.splitext(filename)[0] + '.jpg'
        rgb_img.save(os.path.join(output_folder, jpg_filename), quality=95)


tif_to_jpg(input_dir, output_dir)

input("Done...")
