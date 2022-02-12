"""
Noshin Rahman, Rinoa Malapaya, Aranya Sutharasan
References: https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/cryptology/vigenere_cipher/vigenere.py
References: https://careerkarma.com/blog/python-zip/
https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:online-data-security/xcae6f4a7ff015e7d:data-encryption-techniques/a/symmetric-encryption-techniques
"""
alphabet = "bBaAdDcCfFeEhHgGjJiIlLkKnNmMpPoOrRqQtTsSvVuUxXwWzZyY1234567890~!@#$%^&*()_+{}|:<>?-=[]\;,./. "

""" AT THE TOP, we assign each character in the alphabet variable above a number or index to be mapped to using the zip() 
function, then convert that tuple into a dictionary so that it can be called and searched for later. These dictionaries are used to
create a mapping of the alphabet and will be used for shifting later on. The different dictionaries are for different directions
of mapping.
"""
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def encrypt(message, key):
    encrypted = ""
    split_message = [message[i : i + len(key)] for i in range(0, len(message), len(key))]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
            encrypted += index_to_letter[number]
            i += 1



    return encrypted

""" In the function above, we split up the plaintext into individual characters and assign each letter of the key to it. 
The letters of the key are generated and mapped to each character in the plaintext until the length of the plaintext is
reached using a for loop. This creates a big list filled with pairings of the plaintext to the key called "split_message".
Then, for every pairing in the split_message list, the encrypted value is determined by first searching for the index value
of the plaintext character's position in the alphabet key, doing the same but with the index value of the key, and then 
dividing that by the total length of the alphabet to get the exact position where the plaintext and key meet in the 
alphabet table. The encrypted value of that index is determined by searching in the "index_to_letter" dictionary and is
appended to the initially empty string called "encrypted" and returns it.
"""

def decrypt(cipher, key):
    decrypted = ""
    split_encrypted = [
        cipher[i : i + len(key)] for i in range(0, len(cipher), len(key))
    ]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
            decrypted += index_to_letter[number]
            i += 1
    return decrypted




def main():

    with open('plaintext.txt', 'r') as file:
        message = file.read().replace('\n', '')
    key = "sonnirara"
    #sonnirara is the key

    """-----------------ENCRYPTION--------------------
    """

    translated = ''
    """in the main function, we are opening the txt filed named "plaintext" to be read. We removed all the next lines to get rid of as
    spacing as possible. """
    i = len(message) - 1

    while i >= 0:
        translated = translated + message[i]
        i = i - 1

    encrypted_message = encrypt(translated, key)
    decrypted_message = decrypt(encrypted_message, key)

    """
    The code above flips the plaintext message backwards by declaring a decreasing i value that starts at the length of the 
    message. The i variable is used to point to the last index of the message and appends the value at the index to the empty
    string labelled "translated". As i continuously decreases, all characters of the message/plaintext will be added in 
    reverse order. The reversed plaintext now becomes the message to be inputted into the encryption algorithm.
    """
    #print("Original message: " + message)
    with open('ciphertext.txt', 'w') as f:  #Here, we write a text file and add the encrypted message string to it
        f.writelines(encrypted_message)
    #print("Encrypted message: " + encrypted_message)

    """--------------DECRYPTION----------------------
    """
    not_backwards = ''
    i = len(decrypted_message) - 1

    while i >= 0:           #Here we are undoing the reverse of the plaintext that we did earlier during encryption
        not_backwards = not_backwards + decrypted_message[i]
        i = i - 1
    #print("Decrypted message: " + not_backwards)


main()