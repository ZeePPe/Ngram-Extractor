import pickle 

def save_alignments(all_alignments, file_name): 
    with open(file_name, 'wb') as handle:
        pickle.dump(all_alignments, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_aligments(file_name):
    with open(file_name, 'rb') as handle:
        all_alignments = pickle.load(handle)
    return all_alignments    

def get_ngrams_list(keyword, alphabet_folder=None, n_min=2, n_max=3):
    """
    returns the list of N-grams of the keyword included in the selected alphabet
    nmax define the maximum number of characters for N-gram ()
    """
    ngrams_list= []
    for n in range(n_min,n_max+1):
        for index in range(len(keyword)-n+1):
            ngram = keyword[index:index+n]

            if alphabet_folder is None:
                ngrams_list.append(ngram)
            else:
                if ngram in os.listdir(alphabet_folder):
                    ngrams_list.append(ngram)
    return ngrams_list

