import string

"""
A few methods that decrypts a text encrypted with Affine Cipher. Constants needed
Author: Angela Yang
Date: 1/11/2023
"""

alphabet = list(string.ascii_uppercase)
alphabet.extend([" ", ",", "."])


"""
Reads a cipher text and deciphers it into plain text.
"""


def decryptAffine(filename):
    minv, n, text = transcript(filename)
    return decipher(minv, n, text)


"""
Reads a plain text and encrypts it with Affine Cipher.
"""


def encryptAffine(filename):
    m, n, text = transcript(filename)
    return encrypt(m, n, text)


"""
Reads the file, transfers it into a string and filters it to contain no new lines and only capitalized characters.
Retrieves the two integer keys from the beginning of the text file.
Returns a list containing the key and the text, two integers and a string
Reads a string.
"""


def transcript(filename):
    with open(filename, 'r') as file:
        text = file.read().replace('\n', '')
    # the first word separated by comma is the key
    m = int(text.split(",")[0])
    b = int(text.split(",")[1])
    text = ''.join(text.split(",")[2:])
    return [m, b, ''.join(i.upper()if i.isalpha() else i for i in text)]



"""
Deciphers the text by calculating the corresponding plaintext and returns a string of plain text.
Reads two integers and a string.
"""


def decipher(minv, b, text):
    message = []
    # for each word, deciphers it by the correct key
    for i in text:
        # p = (c-b) * minv mod 26
        print(i, " is " , alphabet[(alphabet.index(i) - b) * minv % 29])
        message.append(alphabet[(alphabet.index(i) - b) * minv % 29])
    return ''.join(message)


"""
Encrypts the text by calculating the corresponding cipher text and returns a string.
Reads two integers and a string.
"""


def encrypt(m, b, text):
    ct = []
    # for each word, encrypts it by the correct key
    for i in text:
        # c = p*m + b mod 26
        ct.append(alphabet[(alphabet.index(i) * m + b) % 29])
    return ''.join(ct)


"""
Test Run
"""

# # transcript
# print(transcript("affine.txt"))
#
# # decipher
# print(decipher(11, 2, "FACNZ"))


open("answer.txt", "w").write(decryptAffine("affine.txt"))

open("answer cipher.txt", "w").write(encryptAffine("affine.txt"))
