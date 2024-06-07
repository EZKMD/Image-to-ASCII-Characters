from PIL import Image
from tqdm import tqdm

def draw(file_location, imag):
    # Accquiring dimensions that will later be used as limits
    width = imag.width
    height = imag.height
    # Opening relevant files
    with open(file_location, "a") as file:  # Open file in append mode
        print("--------------------------------------")
        print("Rendering...")
        # For every y level...
        for y_pixel in tqdm(range(height)):
            if y_pixel != 0: file.write("\n")

            # Replace every x pixel in that y level
            for x_pixel in range(width):
                # Retrieving RGB values of specific pixel
                pixelRGB = imag.getpixel((x_pixel, y_pixel))
                R, G, B = pixelRGB
                # Averaging the RGB values to find the pixels brightness
                brightness = round(sum([R, G, B]) / 3, 1)
                
                # Assigning symbols based on the brightness of pixel
                if brightness <= 31:
                    file.write("#")
                elif brightness <= 62:
                    file.write("&")
                elif brightness <= 93:
                    file.write("%")
                elif brightness <= 124:
                    file.write("+")
                elif brightness <= 155:
                    file.write("-")
                elif brightness <= 186:
                    file.write(";")
                elif brightness <= 217:
                    file.write(",")
                elif brightness <= 248:
                    file.write(".")
                else:
                    file.write(" ")
    print("Done!")
    print("--------------------------------------")

def main():
    # File locations:
    # Image to file to transfer
    imag = Image.open("./media/image5.webp")
    # Text file to write to 
    file_location = "./media/canvas5_a.txt"
    # Converting image to an RGB image, in case of gif file imported
    imag = imag.convert('RGB')
    draw(file_location, imag)

main()
