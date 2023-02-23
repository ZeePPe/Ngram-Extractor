import os
import shutil
import configs as C
import utils
from tqdm import tqdm

if os.path.exists(C.GT_FOLDER):
    shutil.rmtree(C.GT_FOLDER)
os.mkdir(C.GT_FOLDER)

for word_file_name in tqdm(os.listdir(C.WORDS_FOLDER)):
    transcript = word_file_name.split("_")[-1].split(".")[0]

    ngrams = utils.get_ngrams_list(transcript, n_max=C.MAX_NGRAM, n_min=C.MIN_NGRAM)

    with open(os.path.join(C.GT_FOLDER,  word_file_name.split(".")[0]+".txt"), "w") as gt_file:
        for ng in ngrams:
            gt_file.write(ng+"\n")

print("Done!")