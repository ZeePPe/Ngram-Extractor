import os

WORDS_FOLDER = os.path.join("data","words")
GT_FOLDER = os.path.join("data","GT")
OUT_MIM_FOLDER = os.path.join("out","out_align")
OUT_MIM_FILENAME = "all_align.als"

OUT_ALL_NGRAMS_FOLDER =  os.path.join("out","out_all_ngrams")
OUT_NGRAMS_FOLDER =  os.path.join("out","out_ngrams")

TIME_BASEFOLDER =  os.path.join("out","time")
TIME_WORDCORRECTION_FILENAME = "time_align_correction.txt"

PERFORMANCE_BASEFOLDER =  os.path.join("out","performance")
PERFORMANCE_FILENAME = "performance.txt"

# BOX segmenter parame
BOX_IN_TRANSPARENCY_ALPHA = 0.2
BOX_TRANSPARENCY_ALPHA = 0.4
BOX_BORDER = 1 # 
BOX_COLOR = (0,255,0)

#reference height
H = 64

# Ngrams to extract
MIN_NGRAM = 2
MAX_NGRAM = 3

# len ngramfile name
MAX_LEN_NGRAM_NAME = 4

# Main Window
MIN_WIDTH_MAINW = 250
