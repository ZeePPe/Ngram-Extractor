# Ngrams builder
The repo contains the methods to segment words in ngrams.
It takes words image and generate all ngrams included in the imagese.


## Define enviroment
You need to have the anaconda environment manager installed on your computer.
If so, run the command
```conda env create -f environment.yml```
and acrivate the enciroment: 
```conda activate MiMalign```


## Preparation
1. Check all the input folders in the file ```configs.py```.

2. Create a ```"data/words"``` folder which contains the images of words. the name of the file must be lie: 
```
ID_transcript.png
```
Valid images extensions: png, jpg, jpeg

3. Create the ```"data/GT"``` folder by running th ```create_GT.py``` script.

4. Create the data infrastructor by running the script ```create_out_als.py```



## Labelling data

1. You can labell the words by running the ```"segmentation_tool.py.py"``` file
   the tool will display all the words aligned one at a time.
    - With the ENTER key you can move to the next word.
    - With the BACKSPACE key you go back to the previous word (of the same line)
    - With the DEL key you can delete an alignmnt
    - With the 'j' key you can input (in the console for now) the index od the ngram to jump  
    - With the cntrl+s keys you save the state
    - With the cntrl+q keys you can close the GUI (or just with 'q', it depends on your CV2 version)
    
  
   The process generates in the ```time``` folder a file where the total time spent on the correction is reported

   The process also measures the automatic segmentation performance:
   a file will be saved in the ```Performance``` folder.

## Saving ngrams images

1. run the file ```crop_all_ngrams.py``` to generate a single folder with all the ngrams.

2. run the file ```crop_ngrams.py``` to generate a folder containing a subfolder for each word with all the releted ngrams.

## Save the training file
1. run the file  ```create_training_file.py``` to henerate the txt file for the training containing the bounding box position for each ngrams in all the words

# One shot run
You can run all the script in one time running the file
```
run_all.py
```
ATTENTION: The script launches all scripts from scratch overwriting previous progress!