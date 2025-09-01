import re, string



def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    new_list = list(set(lst))
    return new_list





def count_case(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """

    uppercase_count = len(re.findall('[A-Z]',string))
    lowercase_count = len(re.findall('[a-z]',string))
    return lowercase_count,uppercase_count


text = "HellO,World"
count_case(text)




def remove_punctuation(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    translation_table = str.maketrans('','',string.punctuation)
    sentence_clean = sentence.translate(translation_table)
    return sentence_clean

sentence_clean = remove_punctuation("This is not a world.! Plase @ do it.")
sentence_clean



def word_count(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    translation_table = str.maketrans('','',string.punctuation)
    sentence_clean = sentence.translate(translation_table)
    word_list = sentence_clean.split()
    return len(word_list)

word_count("Note : this is an example !!! Good day : I am!! )")