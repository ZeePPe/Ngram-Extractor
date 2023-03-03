print("Creating GT...")
import create_GT

print("\nCreating data infrastructure...")
import create_out_als

print("\n Running the Labelling Tool...")
import segmentation_tool

print("\n Saving all Ngrams...")
import crop_all_ngrams
import crop_all_ngrams_in_one

print("\n Saving all Ngrams in word subfolders...")
import crop_ngrams

print("\n Creating the training file...")
import create_training_file