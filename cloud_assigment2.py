import re
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import nltk 
nltk.download('stopwords')
nltk.download('punkt')

def preprocess_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()  
        text = re.sub(r'\W', ' ', text) 
        tokens = word_tokenize(text) 
        stop_words = set(stopwords.words('english')) 
        filtered_tokens = [word for word in tokens if word not in stop_words]  
    return filtered_tokens

def word_frequency(tokens):
    word_count = Counter(tokens) 
    for word, count in word_count.most_common():  
        print(f"{word}: {count}")

def main():
    file_path = r"paragraphs.txt"
    tokens = preprocess_text(file_path)
    word_frequency(tokens)

if __name__ == "__main__":
    main()
