from PIL import Image
import os
import shutil
from tqdm import tqdm

ORIGINAL_IMAGES_FOLDER = "data/lines/wash"
RGB_IMAGES_OUT_FOLDER = "data/lines_RGB"

if __name__ == "__main__":
    if os.path.exists(RGB_IMAGES_OUT_FOLDER):
        shutil.rmtree(RGB_IMAGES_OUT_FOLDER)
    os.makedirs(RGB_IMAGES_OUT_FOLDER)

    for image_file in tqdm(os.listdir(ORIGINAL_IMAGES_FOLDER)):
        image_in_path = os.path.join(ORIGINAL_IMAGES_FOLDER, image_file)
        image_out_path = os.path.join(RGB_IMAGES_OUT_FOLDER, image_file)
        
        image = Image.open(image_in_path)
        image.load()

        # replace alpha channel with white color
        RGB_image = Image.new('RGB', image.size, (255, 255, 255))
        RGB_image.paste(image, None)

        RGB_image.save(image_out_path)