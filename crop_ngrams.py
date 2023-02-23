import os
import shutil
import cv2
from utils import load_aligments
import configs
from tqdm import tqdm

ALIGNMENT_FILE = os.path.join(configs.OUT_MIM_FOLDER, configs.OUT_MIM_FILENAME)
OUT_FOLDER = configs.OUT_NGRAMS_FOLDER

def crop_all_words(aligns, dst_folder="out"):
    if os.path.exists(dst_folder):
        shutil.rmtree(dst_folder)
    os.mkdir(dst_folder)

    for _, all_lines in tqdm(aligns.items()):
        for word_filename, (boxes, transcriptions) in all_lines.items():
            
            curr_folder_name = word_filename.split(".")[0]
            os.mkdir(os.path.join(dst_folder,curr_folder_name))

            line_img = cv2.imread(os.path.join(configs.WORDS_FOLDER, word_filename), cv2.IMREAD_GRAYSCALE)
             
            inline_pos = 0
            for box, trans in zip(boxes, transcriptions):
                if box[0]==box[1]:
                    print(f"Not possible to save {word_filename}")
                else:
                    if not os.path.exists(os.path.join(dst_folder,curr_folder_name, trans)):
                        os.mkdir(os.path.join(dst_folder, curr_folder_name, trans))
                    n_elem_infolder = len(os.listdir(os.path.join(dst_folder,curr_folder_name, trans)))

                    new_filename = str(n_elem_infolder).zfill(configs.MAX_LEN_NGRAM_NAME) +"."+ word_filename.split(".")[-1]

                    word_img = line_img[: , box[0]:box[1]]
                    cv2.imwrite(os.path.join(dst_folder, curr_folder_name, trans, new_filename), word_img)

                inline_pos += 1




aligns = load_aligments(ALIGNMENT_FILE)
crop_all_words(aligns, dst_folder=OUT_FOLDER)
print("Done!")