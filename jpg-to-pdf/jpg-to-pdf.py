import os
import subprocess
import configparser
import re
import shutil

config = configparser.ConfigParser()
config.read('full/config.ini')
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
        image_format = jpgToPdfConfig['image_format_{}'.format(counter)]
        counter += 1
        image_formats.append(image_format)
    except:
        break

print('Starting Program...')
print('Image File Format Options:')
for format_counter in range(len(image_formats)):
    image_format = image_formats[format_counter]
    print('{0}: {1}.pdf'.format(
        format_counter + 1, image_format))

choice = input('Choose your conversion option (number): ')

try:
    choiceInt = int(choice)
    if choiceInt == 0:
        raise 1
    chosen_format = image_formats[choiceInt - 1]
except:
    input('{} is not a valid option Exiting...'.format(choice))
    exit(1)

print('Chose [{}] {}...'.format(choiceInt, chosen_format))


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


def convert_image_list_to_pdf(images, output_dir, output_name, format):
    images.sort()

    pdf = FPDF(unit='pt', format=format)

    for image in images:
        pdf.add_page()
        pdf.image(image, 0, 0, w=pdf.w_pt, h=pdf.h_pt)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    pdf.output(os.path.join(output_dir, output_name), 'F')


def convert_images_to_pdf(input_dir, output_dir):
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
    images = []

    for filename in os.listdir(input_dir):
        if any(filename.endswith(ext) for ext in image_extensions):
            images.append(os.path.join(input_dir, filename))

    pdfMap = {}

    groupCount = 0
    splitFormat = chosen_format.split("Q")
    finalFormat = ""

    for splitVal in splitFormat:
        if splitVal is not "":
            finalFormat += "(" + splitVal.replace("X", ".") + ")"
            groupCount += 1
        finalFormat += '.'

    finalFormat = finalFormat[:-1]

    for image in images:
        fileName, fileExt = os.path.splitext(image)
        justFileName = os.path.basename(fileName)
        match = re.fullmatch(finalFormat, justFileName)
        if match is None:
            continue

        pdfName = ""
        for i in range(groupCount):
            pdfName += match.group(i + 1)
        print("Funnelling into " + pdfName + ".pdf file " + justFileName)

        if pdfName not in pdfMap:
            pdfMap[pdfName] = []

        pdfMap[pdfName].append(image)

    for pdfName in pdfMap.keys():
        convert_image_list_to_pdf(
            pdfMap[pdfName], output_dir, pdfName + ".pdf", format)


convert_images_to_pdf(input_dir, output_dir)


input("Done...")
