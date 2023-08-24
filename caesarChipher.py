def caesarCipher(s, k):
    # Write your code here
    encoded_message = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = len(alphabet)
    for letter in s:
        if letter in alphabet:
            encoded_index = alphabet.index(letter) + k
            if encoded_index >= n:
                encoded_index %= n
            encoded_message += alphabet[encoded_index]
        elif letter in ALPHABET:
            encoded_index = ALPHABET.index(letter) + k
            if encoded_index >= n:
                encoded_index %= n
            encoded_message += ALPHABET[encoded_index]
        else:
            encoded_message += letter
    return encoded_message
