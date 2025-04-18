import streamlit as st
import random
from math import gcd

# Vigenère Cipher

def vigenere_encrypt(plaintext: str, key: str, alphabet: str) -> str:
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

# Caesar Cipher

def caesar_encrypt_decrypt(text, shift_keys, ifdecrypt):
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

# Primitive Root Calculation

def primitive_root(g, n):
    req_set = {num for num in range(1, n)}
    gen_set = {pow(g, power, n) for power in range(1, n)}
    return req_set == gen_set

def find_primitive_roots(n):
    pri_roots = []
    for g in range(1, n):
        if primitive_root(g, n):
            pri_roots.append(g)
    return pri_roots

def print_mod_expo(n):
    pri_roots = find_primitive_roots(n)
    results = []
    for g in range(1, n):
        result_list = []
        value = 1
        for power in range(1, n):
            value = pow(g, power, n)
            result_list.append(f"{g}^{power} mod {n} = {value}")
            if value == 1 and power < n - 1:
                break
        result_str = ", ".join(result_list)
        if g in pri_roots:
            results.append(f"{result_str} ==> {g} is primitive root of {n}")
        else:
            results.append(f"{result_str}")
    return pri_roots, results

# RSA Encryption

def generate_prime_number():
    while True:
        prime_candidate = random.randint(2**8, 2**9)
        if is_prime(prime_candidate):
            return prime_candidate

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair():
    p = generate_prime_number()
    q = generate_prime_number()
    n = p * q
    totient = (p - 1) * (q - 1)
    e = random.randrange(1, totient)
    g = gcd(e, totient)
    while g != 1:
        e = random.randrange(1, totient)
        g = gcd(e, totient)
    d = pow(e, -1, totient)
    return (e, n), (d, n)

def rsa_encrypt(pk, plaintext):
    key, n = pk
    return [pow(ord(char), key, n) for char in plaintext]

def rsa_decrypt(pk, ciphertext):
    key, n = pk
    return ''.join(chr(pow(char, key, n)) for char in ciphertext)

# Streamlit UI
st.title("Applied Cryptography Project")

cipher_choice = st.sidebar.radio("Choose Method:", ["Vigenère Cipher", "Caesar Cipher", "Primitive Root Calculation", "RSA Encryption"])

if cipher_choice == "Vigenère Cipher":
    st.header("Vigenère Cipher Encryption")
    alphabet = st.text_input("Enter Alphabet:")
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
        result_text = caesar_encrypt_decrypt(text, shift_keys, ifdecrypt=(operation == "Decrypt"))
        st.write(f"### {operation}ed Message:", result_text)

elif cipher_choice == "Primitive Root Calculation":
    st.header("Primitive Root Calculation")
    n = st.number_input("Enter Prime Number:", min_value=2, step=1)
    if st.button("Check"):
        pri_roots, results = print_mod_expo(n)
        for res in results:
            st.write(res)
        st.write(f"List of Primitive Roots: {pri_roots}")

elif cipher_choice == "RSA Encryption":
    st.header("RSA Encryption")
    if st.button("Generate Keys"):
        public_key, private_key = generate_keypair()
        st.session_state["public_key"] = public_key
        st.session_state["private_key"] = private_key
        st.write(f"Public Key: {public_key}")
        st.write(f"Private Key: {private_key}")
    
    message = st.text_input("Enter Message:")
    if st.button("Encrypt"):
        if "public_key" in st.session_state:
            encrypted_msg = rsa_encrypt(st.session_state["public_key"], message)
            st.session_state["encrypted_msg"] = encrypted_msg
            st.write("### Encrypted Message:", encrypted_msg)
    
    if st.button("Decrypt"):
        if "private_key" in st.session_state and "encrypted_msg" in st.session_state:
            decrypted_msg = rsa_decrypt(st.session_state["private_key"], st.session_state["encrypted_msg"])
            st.write("### Decrypted Message:", decrypted_msg)
