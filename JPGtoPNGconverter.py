import sys
import os
from PIL import Image

#grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#check if new/ exists, if not create
if (os.path.exists(output_folder)) is False:
    os.mkdir(output_folder)

#loop through pokedex/
#convert
#save to new/

for file in os.listdir(image_folder):
    img = Image.open(os.path.join(image_folder, file))
    filename = file.split('.')
    target_name = filename[0] + '.png'
    img.save(os.path.join(output_folder, target_name), 'png')