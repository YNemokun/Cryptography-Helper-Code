import matplotlib.pyplot as plt

"""
A few methods that analyze a set of frequencies of a piece of text based on the letters in its key.
This is useful for Vigenere Square ciphers
Author: Angela Yang
Date: 1/9/2023
"""

"""
Returns bar graphs for the frequencies of each letter in the key
"""


def barGraphVigenere(filename, key):
    return graphVigenere(getFrequencyVigenere(transcript(filename), key))


"""
Returns bar graphs for the frequencies of each letter. For Caesar Cipher.
"""


def barGraph(filename):
    return graph(getFrequency(transcript(filename)))


"""
Reads the file, transfers it into a string and filters it to contain no new lines and only capitalized characters
"""


def transcript(filename):
    with open(filename, 'r') as file:
        text = file.read().replace('\n', '')
    return ''.join(i.upper() for i in text if i.isalpha())


"""
Returns a list of frequencies based on key length
"""


def getFrequencyVigenere(text, key_length):
    # marks the letter of the key we are on
    turn = 0
    allFrequencies = []
    while key_length > turn:
        singleFrequency = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
                           'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
                           'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
                           'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
        # skips to every letter that is encrypted with this letter's alphabet
        # [start:stop:step] -- [turn:end:keylength]
        for i in text[turn::key_length]:
            # adds one to its count
            singleFrequency[i] += 1
        # adds to the list of frequencies
        allFrequencies.append(singleFrequency)
        # goes to the next letter
        turn += 1
    return allFrequencies


"""
Returns a dictionary of the frequency of the text. For Caesar Cipher.
"""


def getFrequency(text):
    singleFrequency = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
                       'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
                       'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
                       'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for i in text:
        # adds one to its count
        singleFrequency[i] += 1
    return singleFrequency


"""
Draws a histogram for a list of frequencies
"""


def graphVigenere(freq_list):
    fig, axes = plt.subplots(1, len(freq_list), figsize=(10, 5))
    for i in range(len(freq_list)):
        axes[i].barh(list(freq_list[i].keys()), list(freq_list[i].values()))
        axes[i].set_title(i + 1)
        axes[i].invert_yaxis()
    plt.show()


"""
Draws a histogram for one dictionary of frequencies. For Caesar Cipher.
"""


def graph(freq):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.barh(list(freq.keys()), list(freq.values()))
    ax.set_title("Character Frequencies")
    ax.invert_yaxis()
    plt.show()


"""
Test runs
"""

# # for transcript(text)
# plainText = "cipher.txt"
# upperText = transcript(plainText)
# print(upperText)
#
#
# # for getFrequencies
# key = 2
# freq = getFrequency(upperText, key)
#
# # for graph
# graph(freq)


"""
Full run
"""

barGraph('cipher.txt')
# barGraphVigenere('cipher.txt', 4)
