def word_count(text):
    """Returns the number of words in the given text."""
    words = text.split()  # Split the text into words using spaces
    return len(words)

def words_ordered_by_length(text):
    """Returns an ordered list of words from longest to shortest."""
    words = text.split()  # Split the text into words
    sorted_words = sorted(words, key=len, reverse=True)  # Sort by length, from longest to shortest
    return sorted_words

def words_alphabetically(text):
    """Returns an alphabetically ordered list of words."""
    words = text.split()  
    sorted_words = sorted(words)  # Sort alphabetically
    return sorted_words
