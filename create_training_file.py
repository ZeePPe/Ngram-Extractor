import os
import configs as C
from utils import load_aligments
import cv2
from tqdm import tqdm

ALIGNMENT_FILE = os.path.join(C.OUT_MIM_FOLDER, C.OUT_MIM_FILENAME)


def create_training_file(aligns, dst_folder="out_training"):
    if not os.path.exists(dst_folder):
        os.mkdir(dst_folder)
    with open(os.path.join(C.ANNOTATION_TRAININGFILE_FOLDER, C.ANNOTATION_TRAININGFILENAME), "w") as out_file:
        for _, all_lines in tqdm(aligns.items()):
            for word_filename, (boxes, transcriptions) in all_lines.items():
                if len(boxes) > 0:
                    for box, trans in zip(boxes, transcriptions):
                        line_img = cv2.imread(os.path.join(C.WORDS_FOLDER, word_filename), cv2.IMREAD_GRAYSCALE)
                        word_path = os.path.join(C.ANNOTATION_BASEWORDS_FOLDER,word_filename)
                        x0, x1 = box
                        y0, y1 = 0, line_img.shape[0]
                        out_file.write(f"{word_path},{x0},{y0},{x1},{y1},{trans}\n")


aligns = load_aligments(ALIGNMENT_FILE)
create_training_file(aligns, dst_folder=C.ANNOTATION_TRAININGFILE_FOLDER)
print("Done!")