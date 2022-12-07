import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
def clean_sentences(sentence : str):
    """Take the raw sentence and clean it by removing stopwords and numbers 
    Args:
	sentence (str): sentence to be cleaned

	Returns:
	_type_: list
    """ 
    sentence = re.sub(r'[0-9]', ' ', sentence)    
    stop_words = set(stopwords.words("english"))
    get_words = sentence.lower().split()
    cleaned_word = list(set([word for word in get_words if word not in stop_words]))
    cleaned_sentence = [" ".join(cleaned_word[::-1])]

    return cleaned_sentence



