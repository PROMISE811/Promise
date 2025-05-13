def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Ensure the shift is within 0-25
    shift = shift % 26
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            # Shift character within its case (upper/lower)
            offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - offset + shift) % 26 + offset)
            result += shifted_char
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    
    return result

# Example usage
plaintext = "Hello, World!"
shift_amount = 3

# Encrypt the plaintext
encrypted_text = caesar_cipher(plaintext, shift_amount)
print(f"Encrypted: {encrypted_text}")

# Decrypt the ciphertext
decrypted_text = caesar_cipher(encrypted_text, shift_amount, mode='decrypt')
print(f"Decrypted: {decrypted_text}")
