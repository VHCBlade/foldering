import os
import subprocess
import configparser
import shutil

config = configparser.ConfigParser()
config.read('jpg-to-pdf/config.ini')
jpgToPdfConfig = config['jpg-to-pdf']

input_dir = jpgToPdfConfig["input"]
output_dir = jpgToPdfConfig["output"]

format = jpgToPdfConfig['format']

print("Will be taking images from " + input_dir +
      " and collating them to PDF in " + output_dir)
print("Format will be " + format + "\n")
accept = input("Will this be Okay? [y/n]")
if accept != "y":
    input("Exiting...")
    exit(0)

counter = 1
image_formats = []

while True:
    try:
        image_format = renameConfig['image_format_{}'.format(counter)]
        counter += 1
        conversion_pairs.append(image_format)
    except:
        break

print('Starting Program...')
print('Conversion Options:')
for format_counter in range(len(conversion_pairs)):
    image_format = conversion_pairs[format_counter]
    print('{0}: {1}.pdf'.format(
        format_counter + 1, image_format))


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


try:
    from PIL import Image
except ImportError:
    install('Pillow')
    from PIL import Image

try:
    from fpdf import FPDF
except ImportError:
    install('fpdf')
    from fpdf import FPDF


def convert_images_to_pdf(input_dir, output_dir, output_name):
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
    images = []

    for filename in os.listdir(input_dir):
        if any(filename.endswith(ext) for ext in image_extensions):
            images.append(os.path.join(input_dir, filename))

    convert_image_list_to_pdf(images, output_dir, output_name, format)


def convert_image_list_to_pdf(images, output_dir, output_name, format):
    images.sort()

    pdf = FPDF(unit='pt', format=format)

    # Add images to PDF
    for image in images:
        pdf.add_page()
        pdf.image(image, 0, 0, w=pdf.w_pt, h=pdf.h_pt)

    # Save PDF to output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    pdf.output(os.path.join(output_dir, output_name), 'F')


# Example usage
output_name = 'output.pdf'

convert_images_to_pdf(input_dir, output_dir, output_name)

input("Done...")
