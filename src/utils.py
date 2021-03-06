import nltk

from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize

nltk.download('stopwords')
nltk.download("punkt")

stopwords = set(nltk.corpus.stopwords.words('english'))

lemmatizer = WordNetLemmatizer()


def lower_remove_punctuation(text):
    text = text.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    text_tokens = tokenizer.tokenize(text)
    return ' '.join(text_tokens)


def remove_stop_words(text):
    """
    Function used to remove stop words

    Args:
        text: string

    Returns:
        String without stop words
    """
    text_tokens = word_tokenize(text)
    tokens_without_sw = [w for w in text_tokens if not w in stopwords and w.isalnum()]
    return ' '.join(tokens_without_sw)


def lemmatize(text):
    """
    Function used to lemmatize text

    Args:
        text: string

    Returns:
        Lemmatized string
    """

    text = text.lower()
    text_tokens = word_tokenize(text)
    lemmatized_tokens = [lemmatizer.lemmatize(w) for w in text_tokens]
    return ' '.join(lemmatized_tokens)
