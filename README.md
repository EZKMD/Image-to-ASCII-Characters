Image to ASCII Program

Overview:
This program takes an image and creates an ACII symbol representation of it, pixel for pixel.

How it Works:
It iterates through each line, and within this, each pixel of said line.
It averages the RGB values of a pixel to achieve a brightness value. 
It then writes an ASCII alternative for the brightness level of the pixel into a text file.

User Actions:
The user must change the "file_location" variable and "imag" variable in order to transfer their own images.
Within this project is the media file which contains various images and their ASCII transferred counterparts.
 Documents here conform to an arbitrary naming convention.

Note:
 - Certain images of lengths greater than ~1050 pixels will break due to text file conventions
 - This is not really optimised at all and is essentially the bare bones of such a program.
    - Many improvements can be made.

Features:
 - TQDM module was used to include a progress bar function.
 - There is no user input, all changes to images and locations are made within code.
