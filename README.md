# Applied Cryptography Application

**Course:** [Your Course Name Here]  
**Date:** [Submission Date Here]

## Group Members

- Christine Kyla Belano (Leader)
- Mark Laurence Pama
- Joshua Ean Valera

---

## Introduction

This project is a user-friendly cryptographic application that allows users to encrypt, decrypt, and hash messages or files using a variety of cryptographic algorithms. The purpose of this project is to demonstrate the practical application of cryptography for securing data and communications. Cryptography is essential in today's digital world to ensure confidentiality, integrity, and authenticity of information.

---

## Project Objectives

1. Implement multiple cryptographic algorithms (symmetric, asymmetric, and hashing) for both text and files.
2. Provide an intuitive graphical user interface for easy interaction with cryptographic functions.
3. Educate users about each algorithm by providing accessible information and background within the application.

---

## Discussions

### Application Architecture and UI Choice

The application is built using **Streamlit**, a Python-based framework for creating interactive web applications. Streamlit was chosen for its simplicity, rapid development capabilities, and ability to create clean, responsive UIs with minimal code. The app is organized into four main sections: Symmetric Encryption/Decryption, Asymmetric Encryption/Decryption, Hashing, and Algorithm Information. Each section is accessible via a sidebar navigation menu.

---

### Implemented Cryptographic Algorithms

#### 1. Block Cipher (AES)
- **Type:** Symmetric
- **History/Background:** AES (Advanced Encryption Standard) was established by NIST in 2001 as the successor to DES. It is widely used for secure data encryption.
- **Process:** AES is a block cipher that encrypts data in fixed-size blocks (128 bits) using keys of 128, 192, or 256 bits. It uses multiple rounds of substitution, permutation, and mixing.
- **Library:** PyCryptodome (`Crypto.Cipher.AES`)
- **Integration:** Used for both text and file encryption/decryption. Users provide a key, and the app handles padding and IV management.

#### 2. Stream Cipher (RC4)
- **Type:** Symmetric
- **History/Background:** RC4 was designed by Ron Rivest in 1987 and was widely used in protocols like SSL/TLS and WEP. It is now considered insecure for many uses.
- **Process:** RC4 generates a pseudo-random keystream which is XORed with the plaintext to produce ciphertext.
- **Library:** Custom implementation in Python
- **Integration:** Available for both text and file encryption/decryption. The user provides a key, and the app handles the RC4 process.

#### 3. Vigenère Cipher
- **Type:** Symmetric
- **History/Background:** The Vigenère cipher is a classic polyalphabetic substitution cipher invented in the 16th century. It was considered unbreakable for centuries.
- **Process:** Each letter of the plaintext is shifted by the value of the corresponding letter in the repeating keyword.
- **Library:** Custom implementation in Python
- **Integration:** Used for text encryption/decryption. The user provides a keyword.

#### 4. RSA
- **Type:** Asymmetric
- **History/Background:** RSA was invented in 1977 by Rivest, Shamir, and Adleman. It is one of the first public-key cryptosystems and is widely used for secure data transmission.
- **Process:** RSA uses a pair of keys (public/private) for encryption and decryption based on the mathematical properties of large prime numbers.
- **Library:** PyCryptodome (`Crypto.PublicKey.RSA`, `Crypto.Cipher.PKCS1_OAEP`)
- **Integration:** Used for text encryption/decryption. The app can generate key pairs and allows users to input their own keys.

#### 5. Diffie-Hellman
- **Type:** Asymmetric (Key Exchange)
- **History/Background:** Proposed by Whitfield Diffie and Martin Hellman in 1976, it allows two parties to establish a shared secret over an insecure channel.
- **Process:** Both parties generate private/public keys and exchange public keys. Each computes the shared secret, which can be used as a symmetric key (e.g., for AES).
- **Library:** PyCryptodome (`Crypto.Random.random` for key generation), Python standard library for math
- **Integration:** Used for secure key exchange. The shared secret is used as an AES key for text encryption/decryption in the app.

#### 6. Hashing Functions (SHA-256, SHA-512, MD5, SHA-1)
- **Type:** Hash
- **History/Background:** Hash functions are used to produce a fixed-size digest from arbitrary data. SHA-256 and SHA-512 are part of the SHA-2 family (NIST, 2001). MD5 and SHA-1 are older and now considered insecure for collision resistance.
- **Process:** Input data is processed to produce a unique hash value (digest).
- **Library:** Python standard library (`hashlib`)
- **Integration:** Used for both text and file hashing. Users select the algorithm and input data or upload a file.

---

## How Algorithms Are Integrated

- Each algorithm is accessible via the app's sidebar.
- Users can input text or upload files, select the desired algorithm, and provide necessary keys or parameters.
- The app provides instant feedback and results, with options to download encrypted/decrypted files.
- The "Algorithm Information" section educates users about each algorithm, its background, and its use in the app.

---

## References

- [PyCryptodome Documentation](https://www.pycryptodome.org/)
- [cryptography.io](https://cryptography.io/)
- [Python hashlib Documentation](https://docs.python.org/3/library/hashlib.html)
- [Wikipedia: Advanced Encryption Standard](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
- [Wikipedia: RC4](https://en.wikipedia.org/wiki/RC4)
- [Wikipedia: Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
- [Wikipedia: RSA (cryptosystem)](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [Wikipedia: Diffie–Hellman key exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)
- [Wikipedia: Cryptographic hash function](https://en.wikipedia.org/wiki/Cryptographic_hash_function)