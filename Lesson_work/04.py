"""
Ciphering
"""
ALPHABET = 'abcdefghijklmopqrstuvwxyz  1234567890!@?''/#$%&*()[]:*`'
ALPHABET_LENGHT = len(ALPHABET)


def encrypt(text, shift):
    result = ''
    for char in text:
        idx = ALPHABET.index(char)
        new_idx = (idx + shift) % ALPHABET_LENGHT
        result += ALPHABET[new_idx]

    return result


def decrypt(text, shift):
    result = ''
    for char in text:
        idx = ALPHABET.index(char)
        new_idx = (idx - shift) % ALPHABET_LENGHT
        result += ALPHABET[new_idx]

    return result


def main():
    user_text = input('Enter text to encrypt: ')
    shift = int(input('Enter desired shift: '))

    encrypted_text = encrypt(user_text, shift)

    print('Encrypted message is: ', encrypted_text)

    print('Decrypted message is: ', decrypt(encrypted_text, shift))


main()
