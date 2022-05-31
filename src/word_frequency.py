import pandas as pd
from pathlib import Path

data_path = (
    Path(__file__).parent.parent.absolute() / 'data/word_frequency.csv'
) # Get full path of file on all machines

# Read in word frequency data
word_frequency_data = pd.read_csv(data_path)

# Filtering word df to include only five letter words
word_frequency_data['word']=word_frequency_data['word'].astype(str)
word_frequency_data.drop(word_frequency_data[word_frequency_data['word'].map(len) < 5 ].index, inplace=True) 
word_frequency_data.drop(word_frequency_data[word_frequency_data['word'].map(len) > 5 ].index, inplace=True) 

def calculate_word_frequency(rep):
    '''Calculate the word frequency value for the
    passed string
    
    Arguments:
        rep (str): five-letter word

    Returns:
        int: heuristic value
    '''
    return 1

if __name__ == '__main__':
    print (1)