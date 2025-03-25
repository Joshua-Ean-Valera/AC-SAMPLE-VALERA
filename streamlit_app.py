import streamlit as st
import random
from math import gcd

def mod_inverse(e, phi):
    a, b = e, phi
    x0, x1 = 0, 1
    while a:
        q, b, a = b // a, a, b % a
        x0, x1 = x1 - q * x0, x0
    return x1 + phi if x1 < 0 else x1

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(start=1000, end=5000):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num

def generate_keys():
    p = generate_prime()
    q = generate_prime()
    while p == q:
        q = generate_prime()
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 65537  # Commonly used public exponent
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    
    d = mod_inverse(e, phi)
    
    return (e, n), (d, n)

def encrypt(message, public_key):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher

def decrypt(cipher, private_key):
    d, n = private_key
    message = ''.join([chr(pow(char, d, n)) for char in cipher])
    return message

# Streamlit UI
st.title("RSA Encryption & Decryption")

if "public_key" not in st.session_state or "private_key" not in st.session_state:
    public_key, private_key = generate_keys()
    st.session_state.public_key = public_key
    st.session_state.private_key = private_key
else:
    public_key = st.session_state.public_key
    private_key = st.session_state.private_key

st.write("### Public Key:", public_key)
st.write("### Private Key:", private_key)

message = st.text_input("Enter a message to encrypt:", "Sorry na My Baby")

if st.button("Encrypt"):
    encrypted_message = encrypt(message, public_key)
    st.session_state.encrypted_message = encrypted_message
    st.write("### Encrypted Message:", encrypted_message)

if "encrypted_message" in st.session_state and st.button("Decrypt"):
    decrypted_message = decrypt(st.session_state.encrypted_message, private_key)
    st.write("### Decrypted Message:", decrypted_message)
