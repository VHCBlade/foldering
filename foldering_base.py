import os
import shutil
import re

# Update these to change the directory that you input and output from
input_dir = "input/"
output_dir = "output/"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

regexes_in_order = [
    # Add regexes here. First argument is the folder name, second argument is the regular expression
    ["Misc Gifs", "^.*\.gif$"],
    ["Resumes", "^.*resume.*$"],
    ["Unsorted", ".*"]
]

for file_name in os.listdir(input_dir):
    if os.path.isfile(os.path.join(input_dir, file_name)):

        for regex_pair in regexes_in_order:
            folder_name, regex = regex_pair
            pattern = re.compile(regex, re.IGNORECASE)

            if not bool(pattern.search(file_name)):
                continue

            print("Sorting " + file_name + " into " + folder_name + "...")

            folder_path = os.path.join(output_dir, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Move the file to the appropriate folder
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(folder_path, file_name)
            shutil.copy(input_path, output_path)
            break

input("Done...")
