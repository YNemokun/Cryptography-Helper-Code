import string

"""
A few methods that deciphers a text encrypted with Caesar Cipher. Alphabet needed
Author: Angela Yang
Date: 1/9/2023
"""

"""
Reads a cipher text and deciphers it into plain text.
"""


def decipherCaesar(filename):
    key, text = transcript(filename)
    return decipher(key, text)


"""
Reads the file, transfers it into a string and filters it to contain no new lines and only capitalized characters.
Retrieves the key from the beginning of the text file.
Returns a list containing the key and the text.
Reads a string.
"""


def transcript(filename):
    with open(filename, 'r') as file:
        text = file.read().replace('\n', '')
    # the first word separated by comma is the key
    key = text.split(",")[0].upper()
    text = ''.join(text.split(",")[1:])
    return [key, ''.join(i.upper() for i in text if i.isalpha())]


"""
Returns a list of shifted alphabet by a certain number.
Reads an int.
"""


def shift(n):
    # creates an alphabet with uppercase letters
    normal = list(string.ascii_uppercase)
    newAlphabet = normal[n:]
    newAlphabet.extend(normal[0:n])
    return newAlphabet


"""
Deciphers the text and returns a string of plain text.
Reads two strings.
"""


def decipher(key, text):
    # receives the list of available ciphers
    cipher = shift(ord(key) - 65)
    message = []
    # for each word, deciphers it by the correct key
    for i in text:
        message.append(chr(65 + cipher.index(i)))
    return ''.join(message)


"""
Test Run
"""

# # transcript
# print(transcript("cipher.txt"))

# # shift
# print(shift(3))

# # decipher
# print(decipher("N", "CUYRTZVFERNYYLRDHVINYRAGGBFCVG"))

# # decipherCaesar
# print(decipherCaesar("cipher.txt"))

open("answer.txt", "w").write(decipherCaesar("cipher.txt"))
