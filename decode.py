def caesar_decrypt(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift % 26  # Wrap around the alphabet
            new_char = chr(((ord(char) - ord('a') - shift_amount) % 26) + ord('a'))
            decrypted += new_char
        else:
            decrypted += char  # Non-alphabetic characters remain unchanged
    return decrypted

# Example usage
ciphertext = "iodj{NhbHº_Vfl_DwbH‰…€ßÿÿH‰•ˆßÿÿfÇ…ßÿÿ}"
for i in range(26):  # Try all possible shifts
    print(f"Shift {i}: {caesar_decrypt(ciphertext, i)}")