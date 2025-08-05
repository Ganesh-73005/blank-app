# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class PlayfairCipher:
    def __init__(self, key="KEYWORD"):
        self.key = key.upper().replace('J', 'I')  # J and I are treated as same
        self.matrix = self._create_matrix()
        self.position = self._create_position_map()
    
    def _create_matrix(self):
        """Create the 5x5 Playfair matrix from the key"""
        print(f"\n🔑 Creating Playfair Matrix from key: '{self.key}'")
        print("=" * 50)
        
        # Remove duplicates while preserving order
        key_chars = []
        seen = set()
        for char in self.key:
            if char.isalpha() and char not in seen:
                key_chars.append(char)
                seen.add(char)
        
        print(f"📝 Key characters (duplicates removed): {key_chars}")
        
        # Add remaining alphabet characters
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # No J
        remaining_chars = [char for char in alphabet if char not in seen]
        
        print(f"📝 Remaining alphabet characters: {remaining_chars}")
        
        # Combine key chars with remaining alphabet
        all_chars = key_chars + remaining_chars
        print(f"📝 Final character sequence: {all_chars}")
        
        # Create 5x5 matrix
        matrix = []
        for i in range(5):
            row = all_chars[i*5:(i+1)*5]
            matrix.append(row)
        
        print(f"\n📋 Playfair Matrix:")
        self._print_matrix(matrix)
        
        return matrix
    
    def _create_position_map(self):
        """Create a mapping of character to (row, col) position"""
        position = {}
        for i in range(5):
            for j in range(5):
                position[self.matrix[i][j]] = (i, j)
        return position
    
    def _print_matrix(self, matrix):
        """Pretty print the matrix"""
        print("    0   1   2   3   4")
        print("  ┌───┬───┬───┬───┬───┐")
        for i, row in enumerate(matrix):
            print(f"{i} │ {' │ '.join(row)} │")
            if i < 4:
                print("  ├───┼───┼───┼───┼───┤")
        print("  └───┴───┴───┴───┴───┘")
    
    def _prepare_text(self, text):
        """Clean and prepare text for encryption/decryption"""
        text = text.upper().replace('J', 'I')
        # Remove non-alphabetic characters
        text = ''.join(char for char in text if char.isalpha())
        return text
    
    def _create_pairs(self, text):
        """Create pairs of characters for processing"""
        print(f"\n🔤 Creating character pairs from: '{text}'")
        print("=" * 50)
        
        pairs = []
        i = 0
        while i < len(text):
            if i == len(text) - 1:
                # Last character, pair with X
                pairs.append(text[i] + 'X')
                print(f"📌 Single character '{text[i]}' paired with 'X': {text[i]}X")
                i += 1
            elif text[i] == text[i + 1]:
                # Same characters, insert X between them
                pairs.append(text[i] + 'X')
                print(f"📌 Double character '{text[i]}{text[i+1]}' split with 'X': {text[i]}X")
                i += 1
            else:
                # Normal pair
                pair = text[i] + text[i + 1]
                pairs.append(pair)
                print(f"📌 Normal pair: {pair}")
                i += 2
        
        print(f"\n✅ Final pairs: {pairs}")
        return pairs
    
    def _find_positions(self, char1, char2):
        """Find positions of two characters in the matrix"""
        pos1 = self.position[char1]
        pos2 = self.position[char2]
        print(f"📍 Position of '{char1}': row {pos1[0]}, col {pos1[1]}")
        print(f"📍 Position of '{char2}': row {pos2[0]}, col {pos2[1]}")
        return pos1, pos2
    
    def _encrypt_pair(self, pair):
        """Encrypt a single pair of characters"""
        char1, char2 = pair[0], pair[1]
        pos1, pos2 = self._find_positions(char1, char2)
        
        row1, col1 = pos1
        row2, col2 = pos2
        
        if row1 == row2:
            # Same row - move right (wrap around)
            new_col1 = (col1 + 1) % 5
            new_col2 = (col2 + 1) % 5
            encrypted_char1 = self.matrix[row1][new_col1]
            encrypted_char2 = self.matrix[row2][new_col2]
            print(f"🔄 Same row rule: move right")
            print(f"   '{char1}' -> '{encrypted_char1}' (row {row1}, col {col1} -> col {new_col1})")
            print(f"   '{char2}' -> '{encrypted_char2}' (row {row2}, col {col2} -> col {new_col2})")
            
        elif col1 == col2:
            # Same column - move down (wrap around)
            new_row1 = (row1 + 1) % 5
            new_row2 = (row2 + 1) % 5
            encrypted_char1 = self.matrix[new_row1][col1]
            encrypted_char2 = self.matrix[new_row2][col2]
            print(f"🔄 Same column rule: move down")
            print(f"   '{char1}' -> '{encrypted_char1}' (row {row1} -> {new_row1}, col {col1})")
            print(f"   '{char2}' -> '{encrypted_char2}' (row {row2} -> {new_row2}, col {col2})")
            
        else:
            # Rectangle rule - swap columns
            encrypted_char1 = self.matrix[row1][col2]
            encrypted_char2 = self.matrix[row2][col1]
            print(f"🔄 Rectangle rule: swap columns")
            print(f"   '{char1}' -> '{encrypted_char1}' (row {row1}, col {col1} -> col {col2})")
            print(f"   '{char2}' -> '{encrypted_char2}' (row {row2}, col {col2} -> col {col1})")
        
        encrypted_pair = encrypted_char1 + encrypted_char2
        print(f"✅ Pair '{pair}' encrypted to '{encrypted_pair}'")
        return encrypted_pair
    
    def _decrypt_pair(self, pair):
        """Decrypt a single pair of characters"""
        char1, char2 = pair[0], pair[1]
        pos1, pos2 = self._find_positions(char1, char2)
        
        row1, col1 = pos1
        row2, col2 = pos2
        
        if row1 == row2:
            # Same row - move left (wrap around)
            new_col1 = (col1 - 1) % 5
            new_col2 = (col2 - 1) % 5
            decrypted_char1 = self.matrix[row1][new_col1]
            decrypted_char2 = self.matrix[row2][new_col2]
            print(f"🔄 Same row rule: move left")
            print(f"   '{char1}' -> '{decrypted_char1}' (row {row1}, col {col1} -> col {new_col1})")
            print(f"   '{char2}' -> '{decrypted_char2}' (row {row2}, col {col2} -> col {new_col2})")
            
        elif col1 == col2:
            # Same column - move up (wrap around)
            new_row1 = (row1 - 1) % 5
            new_row2 = (row2 - 1) % 5
            decrypted_char1 = self.matrix[new_row1][col1]
            decrypted_char2 = self.matrix[new_row2][col2]
            print(f"🔄 Same column rule: move up")
            print(f"   '{char1}' -> '{decrypted_char1}' (row {row1} -> {new_row1}, col {col1})")
            print(f"   '{char2}' -> '{decrypted_char2}' (row {row2} -> {new_row2}, col {col2})")
            
        else:
            # Rectangle rule - swap columns
            decrypted_char1 = self.matrix[row1][col2]
            decrypted_char2 = self.matrix[row2][col1]
            print(f"🔄 Rectangle rule: swap columns")
            print(f"   '{char1}' -> '{decrypted_char1}' (row {row1}, col {col1} -> col {col2})")
            print(f"   '{char2}' -> '{decrypted_char2}' (row {row2}, col {col2} -> col {col1})")
        
        decrypted_pair = decrypted_char1 + decrypted_char2
        print(f"✅ Pair '{pair}' decrypted to '{decrypted_pair}'")
        return decrypted_pair
    
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
    
    def _clean_decrypted_text(self, text):
        """Remove padding X characters from decrypted text"""
        # This is a simple cleanup - in practice, you might need more sophisticated logic
        # Remove trailing X
        if text.endswith('X'):
            text = text[:-1]
        
        # Remove X between duplicate characters (this is more complex in real scenarios)
        cleaned = ""
        i = 0
        while i < len(text):
            if i < len(text) - 2 and text[i] == text[i + 2] and text[i + 1] == 'X':
                cleaned += text[i]
                i += 2
            else:
                cleaned += text[i]
                i += 1
        
        return cleaned


def main():
    """Demonstration of the Playfair cipher"""
    print("🎯 PLAYFAIR CIPHER DEMONSTRATION")
    print("=" * 80)
    
    # Initialize cipher with a key
    key = "PLAYFAIRKEY"
    cipher = PlayfairCipher(key)
    
    # Test message
    message = "HELLO WORLD"
    
    print(f"\n📨 Original Message: '{message}'")
    print(f"🔑 Key: '{key}'")
    
    # Encrypt
    encrypted = cipher.encrypt(message)
    
    print("\n" + "=" * 80)
    
    # Decrypt
    decrypted = cipher.decrypt(encrypted)
    
    print(f"\n📊 SUMMARY:")
    print(f"Original:  '{message}'")
    print(f"Encrypted: '{encrypted}'")
    print(f"Decrypted: '{decrypted}'")
    
    # Test with another example
    print("\n" + "=" * 80)
    print("🔄 TESTING WITH ANOTHER EXAMPLE")
    
    message2 = "MEET ME AT DAWN"
    print(f"\n📨 Second Message: '{message2}'")
    
    encrypted2 = cipher.encrypt(message2)
    print("\n" + "=" * 80)
    decrypted2 = cipher.decrypt(encrypted2)
    
    print(f"\n📊 SUMMARY 2:")
    print(f"Original:  '{message2}'")
    print(f"Encrypted: '{encrypted2}'")
    print(f"Decrypted: '{decrypted2}'")


if __name__ == "__main__":
    main()
