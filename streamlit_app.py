import streamlit as st

def vigenere_encrypt(plaintext: str, key: str, alphabet: str) -> str:
    """
    Encrypts plaintext using a Vigenère cipher with custom alphabet.
    
    Args:
        plaintext: Input text containing only characters from the alphabet.
        key: Key containing only characters from the alphabet.
        alphabet: String of unique characters defining character order (index=value).
    
    Returns:
        Encrypted ciphertext string.
    """
    if not alphabet:
        raise ValueError("Alphabet cannot be empty")
    if len(set(alphabet)) != len(alphabet):
        raise ValueError("Alphabet must contain unique characters")
    if not key:
        raise ValueError("Key cannot be empty")
    if not plaintext:
        raise ValueError("Plaintext cannot be empty")
    
    alphabet_set = set(alphabet)
    key = ''.join(c for c in key if c in alphabet_set)
    
    if not key:
        raise ValueError("Key contains no valid characters")
    
    cipher_text = []
    key_index = 0
    
    for char in plaintext:
        if char in alphabet_set:
            char_index = alphabet.index(char)
            key_char = key[key_index % len(key)]
            key_index += 1
            key_val = alphabet.index(key_char)
            new_index = (char_index + key_val) % len(alphabet)
            cipher_text.append(alphabet[new_index])
        else:
            cipher_text.append(char)
    
    return ''.join(cipher_text)

def caesar_encrypt_decrypt(text, shift_keys, ifdecrypt):
    """
    Encrypts or decrypts a text using Caesar Cipher with a list of shift keys.
    
    Args:
        text: The text to encrypt or decrypt.
        shift_keys: A list of integers representing shift values for each character.
        ifdecrypt: Boolean flag to determine decryption.
    
    Returns:
        Transformed text based on encryption or decryption.
    """
    result = []
    shift_keys_len = len(shift_keys)
    
    for i, char in enumerate(text):
        if 32 <= ord(char) <= 126:
            shift = shift_keys[i % shift_keys_len]
            effective_shift = -shift if ifdecrypt else shift
            shifted_char = chr((ord(char) - 32 + effective_shift) % 94 + 32)
            result.append(shifted_char)
        else:
            result.append(char)
    
    return ''.join(result)

# Streamlit UI
st.title("Cipher Encryption Tool")

cipher_choice = st.sidebar.radio("Choose Encryption Method:", ["Vigenère Cipher", "Caesar Cipher"])

if cipher_choice == "Vigenère Cipher":
    st.header("Vigenère Cipher Encryption")
    alphabet = st.text_input("Enter Alphabet:", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    key = st.text_input("Enter Key:")
    plaintext = st.text_input("Enter Plaintext:")
    if st.button("Encrypt"):
        try:
            encrypted_text = vigenere_encrypt(plaintext, key, alphabet)
            st.write("### Encrypted Message:", encrypted_text)
        except ValueError as e:
            st.write("Error:", str(e))

elif cipher_choice == "Caesar Cipher":
    st.header("Caesar Cipher Encryption/Decryption")
    text = st.text_input("Enter Text:")
    shift_keys = list(map(int, st.text_input("Enter Shift Keys (space-separated):").split()))
    operation = st.radio("Choose Operation:", ["Encrypt", "Decrypt"])
    if st.button("Process"):
        if len(shift_keys) < 2 or len(shift_keys) > len(text):
            st.write("Error: Shift keys length must be between 2 and the length of the text.")
        else:
            result_text = caesar_encrypt_decrypt(text, shift_keys, ifdecrypt=(operation == "Decrypt"))
            st.write(f"### {operation}ed Message:", result_text)