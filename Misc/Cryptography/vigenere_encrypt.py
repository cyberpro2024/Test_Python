def vigenere_encrypt(plain_text, secret_key):
    # Prepare input strings: remove spaces and convert to uppercase
    plain_text = plain_text.replace(" ", "").upper()
    secret_key = secret_key.replace(" ", "").upper()
    
    cipher_text = []
    key_length = len(secret_key)
    
    # Iterate over each character in the plaintext
    for i, letter in enumerate(plain_text):
        # Calculate shift value based on the corresponding key letter
        key_char = secret_key[i % key_length]
        shift = ord(key_char) - ord('A')  # Shift is calculated from 'A' (0-25)

        # Encrypt the plaintext letter by shifting it
        if letter.isalpha():  # Encrypt only alphabetic characters
            encrypted_char = chr(((ord(letter) - ord('A') + shift) % 26) + ord('A'))
            cipher_text.append(encrypted_char)
        else:
            cipher_text.append(letter)  # Non-alphabetic characters remain unchanged

    return ''.join(cipher_text)

# User inputs for plaintext and secret key
plain_text = input("Enter the plain text: ")
secret_key = input("Enter the secret key: ")

# Encrypt the plaintext using Vigenere cipher
cipher_text = vigenere_encrypt(plain_text, secret_key)

# Output the cipher text
print(f"Cipher Text: {cipher_text}")
