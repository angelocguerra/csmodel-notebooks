import string
from nltk import pos_tag
from nltk.corpus import wordnet
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer


def to_lower_case(text_series):
    """ Converts characters in each string of a `Series` to lower case.

    Arguments:
        text_series {Series} -- contains input strings
    Returns:
        Series -- contains strings with each character converted to lower case
    """

    # TODO: Implement this function based on the documentation.

    pass


def remove_punctuations(text_series):
    """ Takes in a `Series` of strings and removes punctuations in the text.

    Arguments:
        text_series {Series} -- contains input strings
    Returns:
        list -- contains strings with punctuations removed
    """

    # TODO: Complete this function.

    texts = []

    # TODO: Get all the punctuations to remove, form it into a string, then
    # assign the string to variable `punctuations`
    punctuations = None

    # TODO: For each text in the `Series`, remove the punctuations. Then,
    # append the text without punctuations to the list `texts`.
    for text in text_series:
        pass

    return texts


def remove_stopwords(text_series):
    """ Takes in a `Series` of strings and removes stopwords in the text.

    Arguments:
        text_series {Series} -- contains input strings
    Returns:
        list -- contains strings with stopwords removed
    """

    # TODO: Complete this function.

    texts = []

    # TODO: Get all the stopwords in english, put it in a `set`, and assign the
    # `set` to the variable `stopwords_set`.
    # HINT: Read the documentation of `stopwords` from the `nltk.corpus`
    # package.
    stopwords_set = None

    # TODO: For each text in the `Series`, remove the stopwords. Then, append
    # the text without the stopwords to the list `texts`.
    for text in text_series:
        pass

    return texts


def get_frequent_words(text_series,
                       num_frequent):
    """ Returns the top `num_frequent` words in the dataset.

    Arguments:
        text_series {Series} -- contains input strings
        num_frequent {int} -- number of top frequent words to get from the
        dataset
    Returns:
        list of tuples -- contains the top `num_frequent` words in the dataset.
        Each tuple is represented as (w, c), where w is the word, and c is
        the frequency of the word in the dataset.
    """

    # TODO: Complete this function.

    # TODO: Instantiate a `Counter` object from the `collections` package and
    # assign it to variable `count`.
    count = None

    # TODO: Get each word in all strings in the series then add 1 to its tally
    # in the variable `count`.
    for text in text_series:
        pass

    # TODO: Get the top `num_frequent` frequent words in the dataset and
    # assign it to `frequent_words`.
    # HINT: Read the documentation of `Counter` from the `collections` package.
    frequent_words = None

    return frequent_words


def remove_frequent_words(text_series,
                          num_frequent):
    """ Takes in a `Series` of strings and removes frequent words in the text.

    Arguments:
        text_series {Series} -- contains input strings
        num_frequent {int} -- number of top frequent words to get from the
        dataset and remove from the text
    Returns:
        list -- contains strings with frequent words removed
    """

    # TODO: Complete this function.

    texts = []

    # TODO: Get all the `num_frequent` frequent words, put it in a `set`,
    # and assign the `set` to the variable `frequent_set`.
    # HINT: Use the `get_frequent_words()` function that we have defined.
    frequent_set = None

    # TODO: For each text in the `Series`, remove the frequent words. Then,
    # append the text without the frequent words to the list `texts`.
    for text in text_series:
        pass

    return texts


def stem(text_series):
    """ Takes in a `Series` of strings and performs stemming to each word
    in the string.

    Arguments:
        text_series {Series} -- contains input strings
    Returns:
        list -- contains strings with stemmed words
    """

    # TODO: Complete this function.

    texts = []

    # TODO: Instantiate a `PorterStemmer` object from the `nltk.stem.porter`
    # package and assign it to variable `stemmer`.
    stemmer = None

    # TODO: For each text in the `Series`, stem each word. Then, append the
    # text with stemmed words to the list `texts`.
    # HINT: Read the documentation of `PorterStemmer` from the
    # `nltk.stem.porter` package.
    for text in text_series:
        pass

    return texts


def lemmatize(text_series):
    """ Takes in a `Series` of strings and performs lemmatization to each word
    in the string.

    Arguments:
        text_series {Series} -- contains input strings
    Returns:
        list -- contains strings with lemmatized words
    """

    # TODO: Complete this function.

    texts = []

    # TODO: Instantiate a `WordNetLemmatizer` object from the `nltk.stem`
    # package and assign it to variable `lemmatizer`.
    lemmatizer = None

    map = {'N': wordnet.NOUN,
           'V': wordnet.VERB,
           'J': wordnet.ADJ,
           'R': wordnet.ADV}

    # TODO: For each text in the `Series`, get the Part-of-Speech tag of each
    # word. Then, perform lemmatization to each word given the Part-of-Speech
    # tag. Then, append the text with lemmatized words to the list `texts`.
    # HINT: Read the documentation of `pos_tag` from the `nltk` package.
    # HINT: Read the documentation of `WordNetLemmatizer` from the `nltk.stem`
    # package.
    for text in text_series:
        pass

    return texts
