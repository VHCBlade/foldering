import os
import subprocess
import configparser
import re
import shutil

config = configparser.ConfigParser()
config.read('config.ini')
renameConfig = config['rename']

input_dir = renameConfig["input"]
output_dir = renameConfig["output"]


print("Will be taking files from " + input_dir +
      " and moving and renaming them in " + output_dir)
accept = input("Will this be Okay? [y/n]")
if accept != "y":
    input("Exiting...")
    exit(0)

counter = 1
filenames = []

while True:
    try:
        filename = renameConfig['filename_{}'.format(counter)]
        counter += 1
        filenames.append(filename)
    except:
        break

print('Starting Program...')
print('Rename Options:')
for format_counter in range(len(filenames)):
    filename = filenames[format_counter]
    print('{0}: {1}_<number>.<ext>'.format(
        format_counter + 1, filename))

choice = input('Choose your filename option (number): ')

try:
    choiceInt = int(choice)
    if choiceInt == 0:
        raise 1
    common_filename = filenames[choiceInt - 1]
except:
    input('{} is not a valid option Exiting...'.format(choice))
    exit(1)

print('Chose [{}] {}...'.format(choiceInt, common_filename))


def convert_filenames(input_dir, output_dir):
    count = 1

    for file in os.listdir(input_dir):
        file_ext = os.path.splitext(file)[1]

        new_filename = f'{common_filename}-{count}.{file_ext}'

        input_file_path = os.path.join(input_dir, file)
        output_file_path = os.path.join(output_dir, new_filename)

        shutil.copy(input_file_path, output_file_path)

        count += 1


convert_filenames(input_dir, output_dir)


input("Done...")
