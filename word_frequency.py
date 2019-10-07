import re

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
def remove_punctuation(string):
    """ Takes a string as the argument and removes all characters except letters and spaces"""
    regex = re.compile('[A-Za-z\s]')
    depunctuated_list = [letter for letter in string if regex.match(letter)]
    depunctuated_string = (''.join(depunctuated_list)).lower().replace('\n', ' ')
    return depunctuated_string


def filter_stop_words(string, stop_words):
    """ Takes a depunctuated, lowercase string as the argument and splits it at spaces, then filters out any words that appear in the stop_words list"""
    string_as_list = string.split()
    filtered_list = [word for word in string_as_list if word not in stop_words]
    return ' '.join(filtered_list)
      
    
def create_frequency_dictionary(string):
    """Takes a string and returns a dictionary where the keys are the words in that string and their values are the number of times that word occurs"""
    frequency_dictionary = {}
    string_as_list = string.split()
    for word in string_as_list:
        frequency_dictionary[word] = frequency_dictionary.get(word, 0) + 1
    return frequency_dictionary



def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    def get_frequency(item):
        return item[1]
        
    read_file = open(file, 'r')
    punctuation_removed = remove_punctuation(read_file.read())
    filtered = filter_stop_words(punctuation_removed, STOP_WORDS)
    frequency_dictionary = create_frequency_dictionary(filtered)
    dictionary_items = (frequency_dictionary.items())
    sorted_frequency = sorted(dictionary_items, key=get_frequency, reverse=True)
    for item in sorted_frequency:
        print(item[0] + ' | ' + str(item[1]))

print_word_freq('seneca_falls.txt')


# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)
