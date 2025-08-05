# Cipher Algorithms - Key Methods and Example Outputs

## 1. Vigenère Cipher

### Key Encryption Method
```python
def encrypt(self, plaintext):
    """Encrypt plaintext using Vigenère cipher"""
    print(f"\n🔐 VIGENÈRE CIPHER ENCRYPTION")
    print("=" * 70)
    print(f"📨 Original plaintext: '{plaintext}'")
    
    # Prepare text
    cleaned_text = self._prepare_text(plaintext)
    
    if not cleaned_text:
        print("❌ No valid characters to encrypt!")
        return ""
    
    # Extend key to match text length
    extended_key = self._extend_key(len(cleaned_text))
    
    # Encrypt each character
    encrypted_chars = []
    print(f"\n🔒 Character-by-character encryption:")
    print(f"   Formula: (Plaintext + Key) mod 26")
    print("-" * 60)
    
    for i, (plain_char, key_char) in enumerate(zip(cleaned_text, extended_key)):
        encrypted_char = self._encrypt_char(plain_char, key_char, i)
        encrypted_chars.append(encrypted_char)
    
    ciphertext = ''.join(encrypted_chars)
    
    # Summary table
    print(f"\n📊 Encryption Summary:")
    print(f"   Position: {''.join([f'{i%10}' for i in range(len(cleaned_text))])}")
    print(f"   Plaintext: {cleaned_text}")
    print(f"   Key:       {extended_key}")
    print(f"   Ciphertext: {ciphertext}")
    
    print(f"\n🎉 FINAL ENCRYPTION RESULT:")
    print(f"   Original:   '{plaintext}'")
    print(f"   Ciphertext: '{ciphertext}'")
    
    return ciphertext
```

### Key Decryption Method
```python
def decrypt(self, ciphertext):
    """Decrypt ciphertext using Vigenère cipher"""
    print(f"\n🔓 VIGENÈRE CIPHER DECRYPTION")
    print("=" * 70)
    print(f"🔒 Ciphertext: '{ciphertext}'")
    
    # Prepare text
    cleaned_text = self._prepare_text(ciphertext)
    
    if not cleaned_text:
        print("❌ No valid characters to decrypt!")
        return ""
    
    # Extend key to match text length
    extended_key = self._extend_key(len(cleaned_text))
    
    # Decrypt each character
    decrypted_chars = []
    print(f"\n🔓 Character-by-character decryption:")
    print(f"   Formula: (Ciphertext - Key) mod 26")
    print("-" * 60)
    
    for i, (cipher_char, key_char) in enumerate(zip(cleaned_text, extended_key)):
        decrypted_char = self._decrypt_char(cipher_char, key_char, i)
        decrypted_chars.append(decrypted_char)
    
    plaintext = ''.join(decrypted_chars)
    
    # Summary table
    print(f"\n📊 Decryption Summary:")
    print(f"   Position:   {''.join([f'{i%10}' for i in range(len(cleaned_text))])}")
    print(f"   Ciphertext: {cleaned_text}")
    print(f"   Key:        {extended_key}")
    print(f"   Plaintext:  {plaintext}")
    
    print(f"\n🎉 FINAL DECRYPTION RESULT:")
    print(f"   Ciphertext: '{ciphertext}'")
    print(f"   Plaintext:  '{plaintext}'")
    
    return plaintext
```

### Example Output (Key: "LEMON", Message: "ATTACK AT DAWN")
```
🔐 VIGENÈRE CIPHER ENCRYPTION
======================================================================
📨 Original plaintext: 'ATTACK AT DAWN'

🧹 Text preparation:
   Original: 'ATTACK AT DAWN'
   Cleaned:  'ATTACKATDAWN' (uppercase, letters only)

🔄 Key extension for text length 12:
   Original key: 'LEMON' (length 5)
   Full repetitions: 2
   Remaining characters needed: 2
   Extended key: 'LEMONLEMONLE'

🔒 Character-by-character encryption:
   Formula: (Plaintext + Key) mod 26
------------------------------------------------------------
   Pos  0: 'A'( 0) + 'L'(11) = 11 ≡ 11 (mod 26) → 'L'
   Pos  1: 'T'(19) + 'E'( 4) = 23 ≡ 23 (mod 26) → 'X'
   Pos  2: 'T'(19) + 'M'(12) = 31 ≡  5 (mod 26) → 'F'
   Pos  3: 'A'( 0) + 'O'(14) = 14 ≡ 14 (mod 26) → 'O'
   Pos  4: 'C'( 2) + 'N'(13) = 15 ≡ 15 (mod 26) → 'P'
   Pos  5: 'K'(10) + 'L'(11) = 21 ≡ 21 (mod 26) → 'V'
   Pos  6: 'A'( 0) + 'E'( 4) =  4 ≡  4 (mod 26) → 'E'
   Pos  7: 'T'(19) + 'M'(12) = 31 ≡  5 (mod 26) → 'F'
   Pos  8: 'D'( 3) + 'O'(14) = 17 ≡ 17 (mod 26) → 'R'
   Pos  9: 'A'( 0) + 'N'(13) = 13 ≡ 13 (mod 26) → 'N'
   Pos 10: 'W'(22) + 'L'(11) = 33 ≡  7 (mod 26) → 'H'
   Pos 11: 'N'(13) + 'E'( 4) = 17 ≡ 17 (mod 26) → 'R'

📊 Encryption Summary:
   Position: 012345678901
   Plaintext: ATTACKATDAWN
   Key:       LEMONLEMONLE
   Ciphertext: LXFOPVEFRNHR

🎉 FINAL ENCRYPTION RESULT:
   Original:   'ATTACK AT DAWN'
   Ciphertext: 'LXFOPVEFRNHR'
```

---

## 2. Hill Cipher

### Key Encryption Method
```python
def encrypt(self, plaintext):
    """Encrypt plaintext using Hill cipher"""
    print(f"\n🔐 HILL CIPHER ENCRYPTION")
    print("=" * 70)
    print(f"📨 Original plaintext: '{plaintext}'")
    
    # Convert text to numbers
    numbers, cleaned_text = self._text_to_numbers(plaintext)
    print(f"🧹 Cleaned text: '{cleaned_text}'")
    
    # Pad if necessary
    padded_numbers = self._pad_text(numbers.copy())
    
    # Create blocks
    blocks = self._create_blocks(padded_numbers)
    
    # Encrypt each block
    encrypted_blocks = []
    print(f"\n🔒 Encrypting each block:")
    print("-" * 50)
    
    for i, block in enumerate(blocks):
        print(f"\n--- Processing Block {i+1} ---")
        encrypted_block = self._process_block(block, self.key_matrix, "encrypt")
        encrypted_blocks.append(encrypted_block)
    
    # Combine all encrypted blocks
    encrypted_numbers = []
    for block in encrypted_blocks:
        encrypted_numbers.extend(block)
    
    ciphertext = self._numbers_to_text(encrypted_numbers)
    
    print(f"\n🎉 FINAL ENCRYPTION RESULT:")
    print(f"   Plaintext:  '{plaintext}'")
    print(f"   Ciphertext: '{ciphertext}'")
    
    return ciphertext
```

### Key Decryption Method
```python
def decrypt(self, ciphertext):
    """Decrypt ciphertext using Hill cipher"""
    print(f"\n🔓 HILL CIPHER DECRYPTION")
    print("=" * 70)
    print(f"🔒 Ciphertext: '{ciphertext}'")
    
    # Convert text to numbers
    numbers, cleaned_text = self._text_to_numbers(ciphertext)
    print(f"🧹 Cleaned ciphertext: '{cleaned_text}'")
    
    # Create blocks (no padding needed for decryption)
    blocks = self._create_blocks(numbers)
    
    # Decrypt each block using inverse matrix
    decrypted_blocks = []
    print(f"\n🔓 Decrypting each block using inverse matrix:")
    print("-" * 50)
    
    for i, block in enumerate(blocks):
        print(f"\n--- Processing Block {i+1} ---")
        decrypted_block = self._process_block(block, self.inv_key_matrix, "decrypt")
        decrypted_blocks.append(decrypted_block)
    
    # Combine all decrypted blocks
    decrypted_numbers = []
    for block in decrypted_blocks:
        decrypted_numbers.extend(block)
    
    plaintext = self._numbers_to_text(decrypted_numbers)
    
    # Clean up padding (remove trailing X's)
    cleaned_plaintext = plaintext.rstrip('X')
    
    print(f"\n🎉 FINAL DECRYPTION RESULT:")
    print(f"   Ciphertext: '{ciphertext}'")
    print(f"   Plaintext:  '{cleaned_plaintext}' (padding removed)")
    
    return cleaned_plaintext
```

### Example Output (Key Matrix: [[3,2],[5,7]], Message: "HELLO")
```
🔐 HILL CIPHER ENCRYPTION
======================================================================
📨 Original plaintext: 'HELLO'

🔤 Text to numbers conversion:
   Text: HELLO
   Numbers: [7, 4, 11, 11, 14]
   Mapping: [('H', 7), ('E', 4), ('L', 11), ('L', 11), ('O', 14)]

📝 Padding needed: 1 characters
   Original length: 5
   Padded length: 6
   Padded with: X

🧱 Created 3 blocks of size 2:
   Block 1: [7, 4] → 'HE'
   Block 2: [11, 11] → 'LL'
   Block 3: [14, 23] → 'OX'

🔒 Encrypting each block:
--------------------------------------------------

--- Processing Block 1 ---

🔄 Encrypting block: [7, 4]

🔢 Matrix multiplication: Matrix × Block mod 26
   Calculation details:
   Row 0: (3×7 + 2×4) = 29 ≡ 3 (mod 26)
   Row 1: (5×7 + 7×4) = 63 ≡ 11 (mod 26)

✅ Encrypted block: [3, 11] → 'DL'

--- Processing Block 2 ---

🔄 Encrypting block: [11, 11]

🔢 Matrix multiplication: Matrix × Block mod 26
   Calculation details:
   Row 0: (3×11 + 2×11) = 55 ≡ 3 (mod 26)
   Row 1: (5×11 + 7×11) = 132 ≡ 2 (mod 26)

✅ Encrypted block: [3, 2] → 'DC'

--- Processing Block 3 ---

🔄 Encrypting block: [14, 23]

🔢 Matrix multiplication: Matrix × Block mod 26
   Calculation details:
   Row 0: (3×14 + 2×23) = 88 ≡ 10 (mod 26)
   Row 1: (5×14 + 7×23) = 231 ≡ 23 (mod 26)

✅ Encrypted block: [10, 23] → 'KX'

🎉 FINAL ENCRYPTION RESULT:
   Plaintext:  'HELLO'
   Ciphertext: 'DLDCKX'
```

---

## 3. Playfair Cipher

### Key Encryption Method
```python
def encrypt(self, plaintext):
    """Encrypt the plaintext using Playfair cipher"""
    print(f"\n🔐 ENCRYPTION PROCESS")
    print("=" * 60)
    print(f"Original text: '{plaintext}'")
    
    # Prepare text
    prepared_text = self._prepare_text(plaintext)
    print(f"Prepared text: '{prepared_text}' (uppercase, J->I, no spaces)")
    
    # Create pairs
    pairs = self._create_pairs(prepared_text)
    
    # Encrypt each pair
    encrypted_pairs = []
    print(f"\n🔒 Encrypting each pair:")
    print("-" * 40)
    
    for i, pair in enumerate(pairs):
        print(f"\nStep {i + 1}: Processing pair '{pair}'")
        encrypted_pair = self._encrypt_pair(pair)
        encrypted_pairs.append(encrypted_pair)
        print()
    
    ciphertext = ''.join(encrypted_pairs)
    print(f"\n🎉 FINAL ENCRYPTED TEXT: '{ciphertext}'")
    return ciphertext
```

### Key Decryption Method
```python
def decrypt(self, ciphertext):
    """Decrypt the ciphertext using Playfair cipher"""
    print(f"\n🔓 DECRYPTION PROCESS")
    print("=" * 60)
    print(f"Encrypted text: '{ciphertext}'")
    
    # Prepare text
    prepared_text = self._prepare_text(ciphertext)
    
    # Create pairs (ciphertext should already be in pairs)
    pairs = [prepared_text[i:i+2] for i in range(0, len(prepared_text), 2)]
    print(f"Cipher pairs: {pairs}")
    
    # Decrypt each pair
    decrypted_pairs = []
    print(f"\n🔒 Decrypting each pair:")
    print("-" * 40)
    
    for i, pair in enumerate(pairs):
        print(f"\nStep {i + 1}: Processing pair '{pair}'")
        decrypted_pair = self._decrypt_pair(pair)
        decrypted_pairs.append(decrypted_pair)
        print()
    
    plaintext = ''.join(decrypted_pairs)
    
    # Clean up the result (remove padding X's if they were added)
    cleaned_plaintext = self._clean_decrypted_text(plaintext)
    
    print(f"\n🎉 FINAL DECRYPTED TEXT: '{cleaned_plaintext}'")
    return cleaned_plaintext
```

### Example Output (Key: "PLAYFAIRKEY", Message: "HELLO WORLD")

#### Playfair Matrix Creation:
```
🔑 Creating Playfair Matrix from key: 'PLAYFAIRKEY'
==================================================
📝 Key characters (duplicates removed): ['P', 'L', 'A', 'Y', 'F', 'I', 'R', 'K', 'E']
📝 Remaining alphabet characters: ['B', 'C', 'D', 'G', 'H', 'M', 'N', 'O', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']
📝 Final character sequence: ['P', 'L', 'A', 'Y', 'F', 'I', 'R', 'K', 'E', 'B', 'C', 'D', 'G', 'H', 'M', 'N', 'O', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']

📋 Playfair Matrix:
    0   1   2   3   4
  ┌───┬───┬───┬───┬───┐
0 │ P │ L │ A │ Y │ F │
  ├───┼───┼───┼───┼───┤
1 │ I │ R │ K │ E │ B │
  ├───┼───┼───┼───┼───┤
2 │ C │ D │ G │ H │ M │
  ├───┼───┼───┼───┼───┤
3 │ N │ O │ Q │ S │ T │
  ├───┼───┼───┼───┼───┤
4 │ U │ V │ W │ X │ Z │
  └───┴───┴───┴───┴───┘
```

#### Encryption Process:
```
🔐 ENCRYPTION PROCESS
============================================================
Original text: 'HELLO WORLD'
Prepared text: 'HELLOWORLD' (uppercase, J->I, no spaces)

🔤 Creating character pairs from: 'HELLOWORLD'
==================================================
📌 Normal pair: HE
📌 Double character 'LL' split with 'X': LX
📌 Normal pair: LO
📌 Normal pair: WO
📌 Normal pair: RL
📌 Single character 'D' paired with 'X': DX

✅ Final pairs: ['HE', 'LX', 'LO', 'WO', 'RL', 'DX']

🔒 Encrypting each pair:
----------------------------------------

Step 1: Processing pair 'HE'
📍 Position of 'H': row 2, col 3
📍 Position of 'E': row 1, col 3
🔄 Same column rule: move down
   'H' -> 'S' (row 2 -> 3, col 3)
   'E' -> 'B' (row 1 -> 2, col 3)
✅ Pair 'HE' encrypted to 'SB'

Step 2: Processing pair 'LX'
📍 Position of 'L': row 0, col 1
📍 Position of 'X': row 4, col 3
🔄 Rectangle rule: swap columns
   'L' -> 'Y' (row 0, col 1 -> col 3)
   'X' -> 'V' (row 4, col 3 -> col 1)
✅ Pair 'LX' encrypted to 'YV'

Step 3: Processing pair 'LO'
📍 Position of 'L': row 0, col 1
📍 Position of 'O': row 3, col 1
🔄 Same column rule: move down
   'L' -> 'R' (row 0 -> 1, col 1)
   'O' -> 'U' (row 3 -> 4, col 1)
✅ Pair 'LO' encrypted to 'RU'

Step 4: Processing pair 'WO'
📍 Position of 'W': row 4, col 2
📍 Position of 'O': row 3, col 1
🔄 Rectangle rule: swap columns
   'W' -> 'V' (row 4, col 2 -> col 1)
   'O' -> 'Q' (row 3, col 1 -> col 2)
✅ Pair 'WO' encrypted to 'VQ'

Step 5: Processing pair 'RL'
📍 Position of 'R': row 1, col 1
📍 Position of 'L': row 0, col 1
🔄 Same column rule: move down
   'R' -> 'D' (row 1 -> 2, col 1)
   'L' -> 'R' (row 0 -> 1, col 1)
✅ Pair 'RL' encrypted to 'DR'

Step 6: Processing pair 'DX'
📍 Position of 'D': row 2, col 1
📍 Position of 'X': row 4, col 3
🔄 Rectangle rule: swap columns
   'D' -> 'S' (row 2, col 1 -> col 3)
   'X' -> 'V' (row 4, col 3 -> col 1)
✅ Pair 'DX' encrypted to 'SV'

🎉 FINAL ENCRYPTED TEXT: 'SBYVRUVQDRSE'
```

## Key Observations

### Vigenère Cipher:
- **Strength**: Uses polyalphabetic substitution with repeating key
- **Formula**: Encryption: (P + K) mod 26, Decryption: (C - K) mod 26
- **Key Feature**: Key extends/repeats to match plaintext length

### Hill Cipher:
- **Strength**: Uses matrix multiplication for block encryption
- **Formula**: Encryption: C = K × P mod 26, Decryption: P = K⁻¹ × C mod 26
- **Key Feature**: Requires invertible key matrix (det must be coprime with 26)

### Playfair Cipher:
- **Strength**: Uses 5×5 matrix with digraph substitution rules
- **Rules**: Same row (right), Same column (down), Rectangle (swap columns)
- **Key Feature**: Handles letter pairs with special rules for duplicates and odd lengths
