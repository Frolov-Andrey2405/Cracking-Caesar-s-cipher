def caesar_decrypt(ciphertext, key):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decrypted_text = ''

    for symbol in ciphertext:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num = (num - key) % len(SYMBOLS)
            decrypted_text += SYMBOLS[num]
        else:
            decrypted_text += symbol

    return decrypted_text


def main():
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print('Enter the encrypted Caesar cipher message to hack.')
    ciphertext = input('> ')

    for key in range(len(SYMBOLS)):
        decrypted_text = caesar_decrypt(ciphertext, key)
        print('Key #{}: {}'.format(key, decrypted_text))


if __name__ == "__main__":
    main()
