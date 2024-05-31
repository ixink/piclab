from PIL import Image
import piexif
from PIL.ExifTags import TAGS
import os
from termcolor import colored, cprint

print('''
 ____ ___ ____     _        _    ____  
|  _ \_ _/ ___|   | |      / \  | __ ) 
| |_) | | |       | |     / _ \ |  _ \ 
|  __/| | |___    | |___ / ___ \| |_) |
|_|  |___\____|___|_____/_/   \_\____/ 
''')


print('''______________________________________________
                coded by:ixink(Rayhan Ahmed)
contact me:linkedin.com/in/rayhan-ahmed-uiu
''')
col = colored("Enter the path to the image file: ", "black", "on_blue")
imagename = input(col)

image = Image.open(imagename)

info_dict = {
    "Image Size": image.size,
    "Image Height": image.height,
    "Image Width": image.width,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Image Color Space": image.getcolors(),
    "Image Compression": image.info.get("compression"),
    "Image Palette": image.palette,
    "Image DPI": image.info.get("dpi"),
    "Image Transparency": image.info.get("transparency"),
    "Image ICC Profile": image.info.get("icc_profile"),
}

for label, value in info_dict.items():
    cprint(f"{label:25}: {value}", "black", "on_green")
try:
   exif_info = image.info.get('exif')
   if exif_info:
       gps_data = exif__dict__.get("GPS", {})
       latitude=gps_data.get(piexif.GPSIFD.GPSLatitude)
       longititude = gps_data.get(piexif.GPSIFD.GPSLongitude)
       altitude = gps_data.get(piexif.GPSIFD.GPSAltitude)
       timestamp = gps_data.get(piexif.GPSIFD.GPSTimeStamp)

       def convert_to_degrees(value):
           degrees, munutes, seconds = value
           return degrees + minutes/60 + seconds/3600
       if latitude and longitude:
           lat_degrees = convert_to_degrees(lattitude)
           lon_degrees = convert_to_degrees(longititude)
           print(f"Latitude: {lat_degrees:.6f}, Longititude: {lon_degrees:.6f}")
       if altitude:
           print(f"Altitude: {altitude[0]} meters")
       if timestamp:
           print(f"Timestamp: {':'.join(str(x) for x in timestamp)}")

   else:
     cprint("No GPS Location found in image. Try with another image.", "red")
except Expection as e:
    cprint(f"An error occured: {e}", "red")
msg = int(input("Do you want to Resize Image?\n1. Yes\n2. No\n"))
if msg == 1:
    if os.path.exists(imagename):
        try:
            with image as im:
                cprint(f"Original Image Size: {im.size}", "blue")
            try:
                new_width =int(input("Enter the new width (in pixels): "))
                new_height = int(input("Enter the new height (in pixels): "))
            except ValueError:
                cprint("Invalid input. Please Enter valid integer value.", "red")
                exit()

            resized_image = im.resize((new_width, new_height))
            resized_image.show()
            message =int(input("Do you want to save?\n1. Yes\n2. No\n"))
            if message == 1:
                      output_path = input("Enter the path to save resized image: ")
                      resized_image.save(output_path)
                      cprint(f"Image Saved at {output_path}", "green")
            elif message == 2:
                        cprint("Thank you for using", "green")
            else:
                cprint("Wrong input. Please input 1 or 2 for select option.", "red")
        except Exception as e:
           cprint(f"Error processing the image: {e}", "red")

else:
    cprint("Wrong input. Input 1 or 2.", "red")
