import emoji
import re
import nltk
from nltk import WordPunctTokenizer
from nltk.corpus import stopwords

def remove_emojis(text:str) -> str:
    return emoji.get_emoji_regexp().sub('', text)

def replace_latin(text:str) -> str:
    clean_text = re.sub("[ñ]","n",text)
    clean_text = re.sub("[á]","a",clean_text)
    clean_text = re.sub("[é]","e",clean_text)
    clean_text = re.sub("[í]","i",clean_text)
    clean_text = re.sub("[ó]","o",clean_text)
    clean_text = re.sub("[ú]","u",clean_text)
    return clean_text

def remove_urls(text:str) -> str:
    pattern = r'(https?)(:\/\/)(\S*)'
    return re.sub(pattern, '', text)

def remove_special_characters(text:str) ->str:
    pattern = r'[^a-zA-Z_\s]'
    return re.sub(pattern,'',text)

def remove_stopwords(text:str) -> str:
    sw = stopwords.words('spanish')
    tokenizer = WordPunctTokenizer()
    tokens = tokenizer.tokenize(text)
    clean_tokens = [token for token in tokens if token not in sw and len(token)> 2]
    return " ".join(clean_tokens)

def clean_text(text:str) -> str:
    clean_text = text.lower()
    clean_text = replace_latin(clean_text)
    clean_text = remove_emojis(clean_text)
    clean_text = remove_urls(clean_text)
    clean_text = remove_special_characters(clean_text)
    clean_text = remove_stopwords(clean_text)
    return clean_text
