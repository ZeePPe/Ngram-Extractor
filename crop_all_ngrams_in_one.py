import os
import shutil
import cv2
from utils import load_aligments
import configs
from tqdm import tqdm

ALIGNMENT_FILE = os.path.join(configs.OUT_MIM_FOLDER, configs.OUT_MIM_FILENAME)
OUT_FOLDER = configs.OUT_ALL_NGRAMS_INONE_FOLDER

def crop_all_words(aligns, dst_folder="out"):
    if os.path.exists(dst_folder):
        shutil.rmtree(dst_folder)
    os.mkdir(dst_folder)

    curr_in = 0

    for _, all_lines in tqdm(aligns.items()):
        for word_filename, (boxes, transcriptions) in tqdm(all_lines.items()):
            # leggi immagine
            line_img = cv2.imread(os.path.join(configs.WORDS_FOLDER, word_filename), cv2.IMREAD_GRAYSCALE)

            id_word = word_filename.split("_")[0]
            extension = word_filename.split(".")[-1]
             
            inline_pos = 0
            bi_position = 0
            tri_position = 0
            
            for box, trans in zip(boxes, transcriptions):
                curr_in += 1
                
                if box[0]>=box[1]:
                    print(f"Not possible to save {word_filename} ngram {trans}, ind {curr_in}")
                    print()
                else:
                    name = id_word
                    if len(trans) == 2:
                        name += "-b-"+str(bi_position).zfill(3)
                        bi_position += 1
                    elif len(trans) == 3:
                        name += "-t-"+str(tri_position).zfill(3)
                        tri_position += 1
                    else:
                        name += "-n-"+str(inline_pos).zfill(3)
                        inline_pos += 1
                
                dst_filename = name+"_"+trans+"."+extension
                word_img = line_img[: , box[0]:box[1]]
                cv2.imwrite(os.path.join(dst_folder, dst_filename), word_img)





aligns = load_aligments(ALIGNMENT_FILE)
crop_all_words(aligns, dst_folder=OUT_FOLDER)
print("Done!")