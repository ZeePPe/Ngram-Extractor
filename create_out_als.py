import os
import cv2
from utils import save_alignments
import configs as C
from tqdm import tqdm


OUT_FILE = os.path.join(C.OUT_MIM_FOLDER, C.OUT_MIM_FILENAME)
if not os.path.exists(C.OUT_MIM_FOLDER):
    os.makedirs(C.OUT_MIM_FOLDER)

FIRST_KEY = "words"
all_aligns = {}

all_aligns[FIRST_KEY] = {}
for word_name  in tqdm(os.listdir(C.WORDS_FOLDER)):
    
    ngrams_list = []
    bbox_list = []

    word_transcript = word_name.split("_")[-1].split(".")[0]

    gt_filename = os.path.join(C.GT_FOLDER, word_name.split(".")[0]+".txt")
    
    word_img = cv2.imread(os.path.join(C.WORDS_FOLDER, word_name))
    char_len = round(word_img.shape[1]/len(word_transcript))
    old_ng_len = 0
    curr_ng_counter = 0
    with open(gt_filename, "r") as gt_file:
        for line in gt_file.readlines():
            ng = line.strip()
            if len(ng) != old_ng_len:
                old_ng_len = len(ng)
                curr_ng_counter = 0
            x0 = curr_ng_counter*char_len
            x1 = (curr_ng_counter+len(ng))*char_len
            ngrams_list.append(line.strip())
            bbox_list.append([x0, x1])
            curr_ng_counter += 1

    all_aligns[FIRST_KEY][word_name] = [bbox_list, ngrams_list]

save_alignments(all_aligns, OUT_FILE)
print("Done!")