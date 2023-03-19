# What does it do?

This takes all the files in an input folder and sorts them into folders in the designated output folder. The script uses regular expressions to determine how the sorting is handled.

# How to Run

Make sure you have [Python](https://www.python.org/) installed on your system.

Before you use the script, open it up with notepad or any text editor you want first. Place your input directory in the input_dir = "<Input Directory here>" line and your output directory in the output_dir = "<Output Directory Here>" line.

You'll also need to download FFMPEG and put it into your path. Here are some instructions on how to do this.

# FFMPEG Download Tutorial (by ChatGPT)

Go to the ffmpeg download page at https://ffmpeg.org/download.html and scroll down to the "Windows" section.

Click on the "Windows Builds" link, which will take you to the "Windows Builds" page.

On the "Windows Builds" page, click on the link for the latest version of ffmpeg that corresponds to your operating system (32-bit or 64-bit).

Extract the contents of the downloaded ZIP file to a location on your computer, such as C:\ffmpeg. This will create a folder called ffmpeg-N.N.N-win64-static (or similar), where N.N.N is the version number of ffmpeg.

Add the ffmpeg executable to your system's PATH environment variable so that you can run it from the command prompt or terminal. To do this, follow these steps:

a. Open the Start menu and search for "Environment Variables".

b. Click on "Edit the system environment variables".

c. Click on the "Environment Variables" button at the bottom of the "Advanced" tab.

d. In the "System Variables" section, scroll down and find the "Path" variable. Click "Edit".

e. Click "New" and add the path to the bin folder inside the ffmpeg folder you extracted earlier (e.g., C:\ffmpeg\bin).

f. Click "OK" on all of the windows to save the changes.

To test that ffmpeg is installed correctly, open a new command prompt or terminal window and type ffmpeg. You should see the ffmpeg help output displayed in the console.