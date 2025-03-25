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

# Streamlit UI
st.title("Vigenère Cipher Encryption")

alphabet = st.text_input("Enter Alphabet:")
plaintext = st.text_input("Enter Plaintext:")
key = st.text_input("Enter Key:")

if st.button("Encrypt"):
    try:
        encrypted_text = vigenere_encrypt(plaintext, key, alphabet)
        st.write("### Encrypted Message:", encrypted_text)
    except ValueError as e:
        st.write("Error:", str(e))
