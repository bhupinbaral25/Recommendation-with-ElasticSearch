import re

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

def clean_sentences(sentence : str) -> str:
    """Take the raw sentence and clean it by removing stopwords and numbers 
    Args:
	sentence (str): sentence to be cleaned

	Returns:
	_type_: str
    """ 
    ps = PorterStemmer()
    sentence = re.sub(r'[0-9]', ' ', sentence)    
    stop_words = set(stopwords.words("english"))
    get_words = sentence.lower().split()
    cleaned_word = list(set([ps.stem(word) for word in get_words if word not in stop_words]))
    
    return " ".join(cleaned_word)
