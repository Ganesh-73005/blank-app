class VigenereCipher:
    def __init__(self, key="KEY"):
        """
        Initialize Vigenère Cipher with a key
        key: string key for encryption/decryption
        """
        self.key = key.upper().replace(' ', '')
        self.key = ''.join(c for c in self.key if c.isalpha())  # Keep only letters
        
        if not self.key:
            raise ValueError("❌ Key must contain at least one alphabetic character")
        
        print(f"🔑 Vigenère Cipher initialized with key: '{self.key}'")
        print(f"📏 Key length: {len(self.key)} characters")
        
        # Display key character values
        key_values = [ord(c) - ord('A') for c in self.key]
        key_mapping = [(self.key[i], key_values[i]) for i in range(len(self.key))]
        print(f"🔢 Key character values: {key_mapping}")
        
        # Create and display Vigenère table
        self._create_vigenere_table()
    
    def _create_vigenere_table(self):
        """Create and display the Vigenère table (tabula recta)"""
        print(f"\n📋 Vigenère Table (Tabula Recta):")
        print("    ", end="")
        
        # Print column headers (A-Z)
        for i in range(26):
            print(f"{chr(i + ord('A')):2}", end="")
        print()
        
        # Print separator
        print("   ┌", end="")
        for i in range(26):
            print("──" if i == 25 else "─┬", end="")
        print("┐")
        
        # Print table rows
        for row in range(26):
            row_char = chr(row + ord('A'))
            print(f"{row_char:2} │", end="")
            
            for col in range(26):
                # Each cell contains the encrypted character
                encrypted_char = chr(((row + col) % 26) + ord('A'))
                print(f"{encrypted_char:2}" if col == 25 else f"{encrypted_char} ", end="")
            print("│")
            
            # Print separator between rows (except last)
            if row < 25:
                print("   ├", end="")
                for i in range(26):
                    print("──" if i == 25 else "─┼", end="")
                print("┤")
        
        # Print bottom border
        print("   └", end="")
        for i in range(26):
            print("──" if i == 25 else "─┴", end="")
        print("┘")
        
        print(f"\n💡 How to read the table:")
        print(f"   - Row: Key character")
        print(f"   - Column: Plaintext character")
        print(f"   - Cell: Encrypted character")
    
    def _prepare_text(self, text):
        """Clean and prepare text for processing"""
        original_text = text
        # Convert to uppercase and remove non-alphabetic characters
        cleaned_text = text.upper().replace(' ', '')
        cleaned_text = ''.join(c for c in cleaned_text if c.isalpha())
        
        print(f"🧹 Text preparation:")
        print(f"   Original: '{original_text}'")
        print(f"   Cleaned:  '{cleaned_text}' (uppercase, letters only)")
        
        return cleaned_text
    
    def _extend_key(self, text_length):
        """Extend key to match text length by repeating it"""
        if text_length == 0:
            return ""
        
        # Calculate how many full repetitions we need
        full_repetitions = text_length // len(self.key)
        remaining_chars = text_length % len(self.key)
        
        # Build extended key
        extended_key = self.key * full_repetitions + self.key[:remaining_chars]
        
        print(f"🔄 Key extension for text length {text_length}:")
        print(f"   Original key: '{self.key}' (length {len(self.key)})")
        print(f"   Full repetitions: {full_repetitions}")
        print(f"   Remaining characters needed: {remaining_chars}")
        print(f"   Extended key: '{extended_key}'")
        
        # Show alignment with positions
        print(f"   Position alignment:")
        positions = "".join([f"{i%10}" for i in range(text_length)])
        print(f"   Positions: {positions}")
        print(f"   Key:       {extended_key}")
        
        return extended_key
    
    def _char_to_num(self, char):
        """Convert character to number (A=0, B=1, ..., Z=25)"""
        return ord(char) - ord('A')
    
    def _num_to_char(self, num):
        """Convert number to character (0=A, 1=B, ..., 25=Z)"""
        return chr(num + ord('A'))
    
    def _encrypt_char(self, plain_char, key_char, position):
        """Encrypt a single character using Vigenère cipher"""
        plain_num = self._char_to_num(plain_char)
        key_num = self._char_to_num(key_char)
        
        # Vigenère encryption: (plaintext + key) mod 26
        encrypted_num = (plain_num + key_num) % 26
        encrypted_char = self._num_to_char(encrypted_num)
        
        print(f"   Pos {position:2}: '{plain_char}'({plain_num:2}) + '{key_char}'({key_num:2}) = {plain_num + key_num:2} ≡ {encrypted_num:2} (mod 26) → '{encrypted_char}'")
        
        return encrypted_char
    
    def _decrypt_char(self, cipher_char, key_char, position):
        """Decrypt a single character using Vigenère cipher"""
        cipher_num = self._char_to_num(cipher_char)
        key_num = self._char_to_num(key_char)
        
        # Vigenère decryption: (ciphertext - key) mod 26
        decrypted_num = (cipher_num - key_num) % 26
        decrypted_char = self._num_to_char(decrypted_num)
        
        print(f"   Pos {position:2}: '{cipher_char}'({cipher_num:2}) - '{key_char}'({key_num:2}) = {cipher_num - key_num:2} ≡ {decrypted_num:2} (mod 26) → '{decrypted_char}'")
        
        return decrypted_char
    
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
    
    def analyze_key_pattern(self, text_length):
        """Analyze how the key repeats for a given text length"""
        print(f"\n🔍 KEY PATTERN ANALYSIS for text length {text_length}")
        print("-" * 50)
        
        extended_key = self._extend_key(text_length)
        
        # Show key repetition pattern
        print(f"Key repetition pattern:")
        for i in range(0, text_length, 10):
            end_pos = min(i + 10, text_length)
            positions = "".join([f"{j%10}" for j in range(i, end_pos)])
            key_segment = extended_key[i:end_pos]
            print(f"   Pos {i:2}-{end_pos-1:2}: {positions}")
            print(f"   Key:     {key_segment}")
            print()
        
        # Key frequency analysis
        key_freq = {}
        for char in extended_key:
            key_freq[char] = key_freq.get(char, 0) + 1
        
        print(f"Key character frequency:")
        for char in sorted(key_freq.keys()):
            count = key_freq[char]
            percentage = (count / len(extended_key)) * 100
            print(f"   '{char}': {count} times ({percentage:.1f}%)")
    
    def encrypt_with_visualization(self, plaintext):
        """Encrypt with step-by-step table visualization"""
        print(f"\n🎨 VIGENÈRE ENCRYPTION WITH TABLE VISUALIZATION")
        print("=" * 70)
        
        cleaned_text = self._prepare_text(plaintext)
        if not cleaned_text:
            return ""
        
        extended_key = self._extend_key(len(cleaned_text))
        
        print(f"\n🔍 Step-by-step table lookup:")
        encrypted_chars = []
        
        for i, (plain_char, key_char) in enumerate(zip(cleaned_text, extended_key)):
            plain_num = self._char_to_num(plain_char)
            key_num = self._char_to_num(key_char)
            encrypted_num = (plain_num + key_num) % 26
            encrypted_char = self._num_to_char(encrypted_num)
            
            print(f"\n--- Step {i+1}: Encrypting '{plain_char}' with key '{key_char}' ---")
            print(f"Table lookup: Row '{key_char}' (row {key_num}), Column '{plain_char}' (col {plain_num})")
            print(f"Result: {key_num} + {plain_num} = {key_num + plain_num} ≡ {encrypted_num} (mod 26) = '{encrypted_char}'")
            
            encrypted_chars.append(encrypted_char)
        
        ciphertext = ''.join(encrypted_chars)
        print(f"\n✅ Final result: '{ciphertext}'")
        return ciphertext


def demonstrate_frequency_analysis():
    """Demonstrate why Vigenère is more secure than Caesar cipher"""
    print(f"\n🔬 FREQUENCY ANALYSIS DEMONSTRATION")
    print("=" * 70)
    
    # Sample text with repeated patterns
    text = "ATTACKATDAWN" * 3  # Repeat to show pattern
    key = "KEY"
    
    cipher = VigenereCipher(key)
    encrypted = cipher.encrypt(text)
    
    print(f"\n📊 Character frequency in plaintext:")
    freq_plain = {}
    for char in text:
        freq_plain[char] = freq_plain.get(char, 0) + 1
    
    for char in sorted(freq_plain.keys()):
        count = freq_plain[char]
        percentage = (count / len(text)) * 100
        print(f"   '{char}': {count} times ({percentage:.1f}%)")
    
    print(f"\n📊 Character frequency in ciphertext:")
    freq_cipher = {}
    for char in encrypted:
        freq_cipher[char] = freq_cipher.get(char, 0) + 1
    
    for char in sorted(freq_cipher.keys()):
        count = freq_cipher[char]
        percentage = (count / len(encrypted)) * 100
        print(f"   '{char}': {count} times ({percentage:.1f}%)")
    
    print(f"\n💡 Notice how the frequency distribution is more even in the ciphertext!")
    print(f"   This makes Vigenère much harder to break than simple substitution ciphers.")


def main():
    """Demonstration of the Vigenère cipher"""
    print("🎯 VIGENÈRE CIPHER DEMONSTRATION")
    print("=" * 80)
    
    # Example 1: Basic encryption/decryption
    print(f"\n📊 EXAMPLE 1: Basic Vigenère Cipher")
    print("-" * 40)
    
    key1 = "LEMON"
    cipher1 = VigenereCipher(key1)
    
    message1 = "ATTACK AT DAWN"
    print(f"\n📨 Message: '{message1}'")
    
    # Encrypt
    encrypted1 = cipher1.encrypt(message1)
    
    print("\n" + "="*80)
    
    # Decrypt
    decrypted1 = cipher1.decrypt(encrypted1)
    
    print(f"\n📊 SUMMARY 1:")
    print(f"Original:  '{message1}'")
    print(f"Key:       '{key1}'")
    print(f"Encrypted: '{encrypted1}'")
    print(f"Decrypted: '{decrypted1}'")
    
    # Example 2: Different key length
    print(f"\n\n📊 EXAMPLE 2: Shorter Key")
    print("-" * 40)
    
    key2 = "KEY"
    cipher2 = VigenereCipher(key2)
    
    message2 = "HELLO WORLD"
    print(f"\n📨 Message: '{message2}'")
    
    # Show key pattern analysis
    cipher2.analyze_key_pattern(len(message2.replace(' ', '')))
    
    # Encrypt with visualization
    encrypted2 = cipher2.encrypt_with_visualization(message2)
    
    print("\n" + "="*80)
    
    # Decrypt
    decrypted2 = cipher2.decrypt(encrypted2)
    
    print(f"\n📊 SUMMARY 2:")
    print(f"Original:  '{message2}'")
    print(f"Key:       '{key2}'")
    print(f"Encrypted: '{encrypted2}'")
    print(f"Decrypted: '{decrypted2}'")
    
    # Example 3: Longer message
    print(f"\n\n📊 EXAMPLE 3: Longer Message")
    print("-" * 40)
    
    key3 = "CIPHER"
    cipher3 = VigenereCipher(key3)
    
    message3 = "MEET ME AT THE PARK AT MIDNIGHT"
    encrypted3 = cipher3.encrypt(message3)
    decrypted3 = cipher3.decrypt(encrypted3)
    
    print(f"\n📊 SUMMARY 3:")
    print(f"Original:  '{message3}'")
    print(f"Key:       '{key3}'")
    print(f"Encrypted: '{encrypted3}'")
    print(f"Decrypted: '{decrypted3}'")
    
    # Frequency analysis demonstration
    demonstrate_frequency_analysis()
    
    # Example 4: Show what happens with invalid key
    print(f"\n\n📊 EXAMPLE 4: Error Handling")
    print("-" * 40)
    
    try:
        invalid_cipher = VigenereCipher("123")
    except ValueError as e:
        print(f"❌ Caught error: {e}")
        print("💡 Keys must contain alphabetic characters!")


if __name__ == "__main__":
    main()
