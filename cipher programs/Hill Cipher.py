import string

"""
A few methods that decrypts a text encrypted with Hill Cipher. Key array needed
Author: Angela Yang
Date: 1/12/2023
"""

alphabet = list(string.ascii_uppercase)
alphabet.extend([" ", ",", "."])

"""
Reads a cipher text and decrypts it into plain text.
"""


def decryptHill(filename):
    keyinv, text = transcript(filename)
    return decrypt(keyinv, text)


"""
Reads a plain text and encrypts it with hill Cipher.
"""


def encryptHill(filename):
    key, text = transcript(filename)
    return encrypt(key, text)


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
    key = eval(text.split(";")[0])
    text = ''.join(text.split(";")[1:])
    return [key, ''.join(i.upper() if i.isalpha() else i for i in text)]



"""
Constructs an array from the text. Reads a string and returns a list
"""


def formArray(text):
    # form an array
    arr = [[0] * ((len(text) + 1) // 2) for i in range(2)]
    t = 0
    for c in range(len(arr[0])):
        for r in range(len(arr)):
            arr[r][c] = alphabet.index(text[t])
            t += 1
            # when to quit
            if t >= len(text):
                print("formatted arr  from 14" , text, " : ", arr)
                return arr


"""
Constructs a piece of text from the array. Reads a list and returns a string
"""


def formText(arr):
    text = []
    for c in range(len(arr[0])):
        for r in range(len(arr)):
            text.append(alphabet[arr[r][c]])
    return ''.join(text)


"""
Constructs a piece of text from the array. Reads a list and returns a string
"""


def formTextEncrypt(arr):
    text = []
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            text.append(alphabet[arr[r][c]])
    return ''.join(text)

"""
Decrypts the text by calculating the corresponding plaintext and returns a string of plain text.
Reads a list and a string.
"""


def decrypt(keyinv, text):
    # obtains an array of cipher text
    ctarr = formArray(text)
    pt = [[0] * len(ctarr[0]) for i in range(2)]
    # [a,b] * [[c],[d]] = [[a*c + b*d]]
    # calculate the pt number
    for r in range(len(keyinv)):
        # row * col
        for c in range(len(ctarr[0])):
            pt[r][c] = (keyinv[r][0] * ctarr[0][c] + keyinv[r][1] * ctarr[1][c]) % 29
    # encrypts it back to text
    print("pt: ", pt)
    return formText(pt)


"""
Encrypts the text by calculating the corresponding cipher text and returns a string.
Reads an array of arrays and a string.
"""


def encrypt(key, text):
    # obtains an array of plain text
    ptarr = formArray(text)
    ct = [[0] * len(ptarr[0]) for i in range(2)]
    # [a,b] * [[c],[d]] = [[a*c + b*d]]
    # calculate the ct number
    for r in range(len(key)):
        # row * col
        for c in range(len(ptarr[0])):
            ct[r][c] = (key[r][0] * ptarr[0][c] + key[r][1] * ptarr[1][c]) % 29
    # encrypts it back to text
    print("ct: ", ct)
    return formText(ct)


"""
Test Run
"""

# transcript
# print(transcript("hill.txt"))
#
# # decrypt
# print(decrypt(11, 2, "FACNZ"))
#
# # alphabet
# print(alphabet)
#
# # formArray
# formArray("ABCDEFG .,")

# # form text
# print(formText([[0,2],[1,3]]))

# # encrypt
# print(encrypt([[13,4],[1,3]], "HELLO, JIM"))

# # decrypt
# print(decrypt([[15, 9], [24, 7]], "UTNPAI YHP"))

open("answer.txt", "w").write(decryptHill("Hill.txt"))

open("answer cipher.txt", "w").write(encryptHill("Hill.txt"))
