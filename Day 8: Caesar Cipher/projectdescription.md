# Caesar Cipher

Welcome to the Caesar Cipher! This Python script allows users to encrypt and decrypt messages using the Caesar Cipher algorithm. Encrypt your messages to keep them secure or decrypt encoded messages to reveal their contents.

## How it Works

1. **Alphabet:**
   - The script initializes a list representing the English alphabet, both lowercase and uppercase.

2. **Caesar Cipher Function:**
   - The `caesar()` function performs the encryption or decryption process based on the given parameters:
     - `start_text`: The original message to be encrypted or decrypted.
     - `shift_amount`: The number of positions to shift each letter in the alphabet.
     - `cipher_direction`: The direction of the cipher process, either "encode" or "decode".

3. **Input and Output:**
   - Users are prompted to choose whether to encrypt or decrypt a message.
   - They enter the message and specify the shift amount for the encryption or decryption process.
   - The script then displays the encrypted or decrypted result.

## Features

- **Input Validation:** The script handles input validation for the shift amount and ensures the program continues to work even if the shift number is greater than 26.
- **Maintaining Symbols:** Numbers, symbols, and spaces in the original message are preserved during encryption and decryption.
- **Restart Option:** Users can choose to restart the cipher program to encrypt or decrypt additional messages without rerunning the script.

## Usage

1. **Initialize the Script:**
   - Run the Python script to start the Caesar Cipher program.

2. **Input Parameters:**
   - Choose the direction of the cipher process: "encode" or "decode".
   - Enter the message to be encrypted or decrypted.
   - Specify the shift amount for the cipher process.

3. **Restart Option:**
   - After encrypting or decrypting a message, users can choose to restart the program to perform additional operations.
