# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import numpy as np
from math import gcd

class HillCipher:
    def __init__(self, key_matrix):
        """
        Initialize Hill Cipher with a key matrix
        key_matrix: 2D list or numpy array representing the key matrix
        """
        self.key_matrix = np.array(key_matrix, dtype=int)
        self.n = len(key_matrix)  # Size of the matrix (n x n)
        
        print(f"🔑 Hill Cipher initialized with {self.n}x{self.n} key matrix:")
        self._print_matrix(self.key_matrix, "Key Matrix")
        
        # Check if key matrix is valid (determinant must be coprime with 26)
        det = int(np.round(np.linalg.det(self.key_matrix))) % 26
        print(f"🔢 Determinant of key matrix: {det}")
        
        if gcd(det, 26) != 1:
            raise ValueError(f"❌ Key matrix is not valid! Determinant {det} is not coprime with 26")
        
        print(f"✅ Key matrix is valid (gcd({det}, 26) = 1)")
        
        # Calculate inverse matrix for decryption
        self.inv_key_matrix = self._matrix_inverse_mod26()
        
    def _print_matrix(self, matrix, title="Matrix"):
        """Pretty print a matrix"""
        print(f"\n📋 {title}:")
        rows, cols = matrix.shape
        
        # Print column headers
        print("    ", end="")
        for j in range(cols):
            print(f"{j:4}", end="")
        print()
        
        # Print separator
        print("   ┌", end="")
        for j in range(cols):
            print("────" if j == cols-1 else "───┬", end="")
        print("┐")
        
        # Print matrix rows
        for i in range(rows):
            print(f"{i:2} │", end="")
            for j in range(cols):
                print(f"{matrix[i][j]:3}", end=" │" if j == cols-1 else " ")
            print()
            
            # Print separator between rows (except last)
            if i < rows - 1:
                print("   ├", end="")
                for j in range(cols):
                    print("────" if j == cols-1 else "───┼", end="")
                print("┤")
        
        # Print bottom border
        print("   └", end="")
        for j in range(cols):
            print("────" if j == cols-1 else "───┴", end="")
        print("┘")
    
    def _extended_gcd(self, a, b):
        """Extended Euclidean Algorithm"""
        if a == 0:
            return b, 0, 1
        gcd_val, x1, y1 = self._extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd_val, x, y
    
    def _mod_inverse(self, a, m=26):
        """Find modular inverse of a modulo m"""
        gcd_val, x, _ = self._extended_gcd(a % m, m)
        if gcd_val != 1:
            raise ValueError(f"Modular inverse of {a} mod {m} doesn't exist")
        return (x % m + m) % m
    
    def _matrix_inverse_mod26(self):
        """Calculate inverse of key matrix modulo 26"""
        print(f"\n🔄 Calculating inverse matrix for decryption:")
        
        det = int(np.round(np.linalg.det(self.key_matrix))) % 26
        print(f"📊 Determinant mod 26: {det}")
        
        det_inv = self._mod_inverse(det, 26)
        print(f"🔢 Modular inverse of determinant: {det_inv}")
        
        # Calculate adjugate matrix
        if self.n == 2:
            # For 2x2 matrix: adj = [[d, -b], [-c, a]]
            a, b = self.key_matrix[0]
            c, d = self.key_matrix[1]
            adj_matrix = np.array([[d, -b], [-c, a]])
        else:
            # For larger matrices, use numpy's approach with cofactor matrix
            adj_matrix = np.round(np.linalg.det(self.key_matrix) * np.linalg.inv(self.key_matrix)).astype(int)
        
        print(f"📋 Adjugate matrix:")
        self._print_matrix(adj_matrix, "Adjugate Matrix")
        
        # Calculate inverse: inv = (det_inv * adj) mod 26
        inv_matrix = (det_inv * adj_matrix) % 26
        
        print(f"🎯 Inverse matrix calculation: ({det_inv} * adj_matrix) mod 26")
        self._print_matrix(inv_matrix, "Inverse Key Matrix")
        
        # Verify the inverse
        verification = (self.key_matrix @ inv_matrix) % 26
        print(f"✅ Verification (Key × Inverse mod 26):")
        self._print_matrix(verification, "Verification Matrix")
        
        return inv_matrix
    
    def _text_to_numbers(self, text):
        """Convert text to numbers (A=0, B=1, ..., Z=25)"""
        text = text.upper().replace(' ', '').replace('J', 'I')  # Remove spaces, J->I
        text = ''.join(c for c in text if c.isalpha())  # Keep only letters
        
        numbers = [ord(c) - ord('A') for c in text]
        print(f"🔤 Text to numbers conversion:")
        print(f"   Text: {text}")
        print(f"   Numbers: {numbers}")
        
        # Show character mapping
        char_mapping = [(text[i], numbers[i]) for i in range(len(text))]
        print(f"   Mapping: {char_mapping}")
        
        return numbers, text
    
    def _numbers_to_text(self, numbers):
        """Convert numbers back to text"""
        text = ''.join(chr(num + ord('A')) for num in numbers)
        print(f"🔤 Numbers to text conversion:")
        print(f"   Numbers: {numbers}")
        print(f"   Text: {text}")
        return text
    
    def _pad_text(self, numbers):
        """Pad text to make length divisible by matrix size"""
        original_length = len(numbers)
        remainder = len(numbers) % self.n
        
        if remainder != 0:
            padding_needed = self.n - remainder
            # Pad with 'X' (23)
            numbers.extend([23] * padding_needed)  # X = 23
            print(f"📝 Padding needed: {padding_needed} characters")
            print(f"   Original length: {original_length}")
            print(f"   Padded length: {len(numbers)}")
            print(f"   Padded with: {'X' * padding_needed}")
        else:
            print(f"📝 No padding needed (length {original_length} is divisible by {self.n})")
        
        return numbers
    
    def _create_blocks(self, numbers):
        """Create blocks of size n from the number list"""
        blocks = []
        for i in range(0, len(numbers), self.n):
            block = numbers[i:i+self.n]
            blocks.append(block)
        
        print(f"🧱 Created {len(blocks)} blocks of size {self.n}:")
        for i, block in enumerate(blocks):
            block_text = ''.join(chr(num + ord('A')) for num in block)
            print(f"   Block {i+1}: {block} → '{block_text}'")
        
        return blocks
    
    def _process_block(self, block, matrix, operation="encrypt"):
        """Process a single block with the given matrix"""
        block_vector = np.array(block).reshape(-1, 1)
        
        print(f"\n🔄 {operation.capitalize()}ing block: {block}")
        print(f"📊 Block as column vector:")
        self._print_matrix(block_vector, "Block Vector")
        
        # Matrix multiplication
        result_vector = (matrix @ block_vector) % 26
        
        print(f"🔢 Matrix multiplication: Matrix × Block mod 26")
        print(f"   Calculation details:")
        for i in range(self.n):
            calculation = " + ".join([f"{matrix[i][j]}×{block[j]}" for j in range(self.n)])
            result_before_mod = sum(matrix[i][j] * block[j] for j in range(self.n))
            result_after_mod = result_before_mod % 26
            print(f"   Row {i}: ({calculation}) = {result_before_mod} ≡ {result_after_mod} (mod 26)")
        
        result_block = result_vector.flatten().tolist()
        result_text = ''.join(chr(num + ord('A')) for num in result_block)
        
        print(f"📊 Result vector:")
        self._print_matrix(result_vector, "Result Vector")
        print(f"✅ {operation.capitalize()}ed block: {result_block} → '{result_text}'")
        
        return result_block
    
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


def main():
    """Demonstration of the Hill cipher"""
    print("🎯 HILL CIPHER DEMONSTRATION")
    print("=" * 80)
    
    # Example 1: 2x2 Hill Cipher
    print(f"\n📊 EXAMPLE 1: 2×2 Hill Cipher")
    print("-" * 40)
    
    key_matrix_2x2 = [[3, 2], [5, 7]]
    cipher_2x2 = HillCipher(key_matrix_2x2)
    
    message1 = "HELLO"
    print(f"\n📨 Message: '{message1}'")
    
    # Encrypt
    encrypted1 = cipher_2x2.encrypt(message1)
    
    print("\n" + "="*80)
    
    # Decrypt
    decrypted1 = cipher_2x2.decrypt(encrypted1)
    
    print(f"\n📊 SUMMARY 1:")
    print(f"Original:  '{message1}'")
    print(f"Encrypted: '{encrypted1}'")
    print(f"Decrypted: '{decrypted1}'")
    
    # Example 2: 3x3 Hill Cipher
    print(f"\n\n📊 EXAMPLE 2: 3×3 Hill Cipher")
    print("-" * 40)
    
    key_matrix_3x3 = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
    cipher_3x3 = HillCipher(key_matrix_3x3)
    
    message2 = "MATHEMATICS"
    print(f"\n📨 Message: '{message2}'")
    
    # Encrypt
    encrypted2 = cipher_3x3.encrypt(message2)
    
    print("\n" + "="*80)
    
    # Decrypt
    decrypted2 = cipher_3x3.decrypt(encrypted2)
    
    print(f"\n📊 SUMMARY 2:")
    print(f"Original:  '{message2}'")
    print(f"Encrypted: '{encrypted2}'")
    print(f"Decrypted: '{decrypted2}'")
    
    # Example 3: Another 2x2 example with different message
    print(f"\n\n📊 EXAMPLE 3: Another 2×2 Hill Cipher")
    print("-" * 40)
    
    key_matrix_simple = [[1, 2], [3, 4]]
    try:
        cipher_simple = HillCipher(key_matrix_simple)
        message3 = "ATTACK AT DAWN"
        encrypted3 = cipher_simple.encrypt(message3)
        decrypted3 = cipher_simple.decrypt(encrypted3)
        
        print(f"\n📊 SUMMARY 3:")
        print(f"Original:  '{message3}'")
        print(f"Encrypted: '{encrypted3}'")
        print(f"Decrypted: '{decrypted3}'")
        
    except ValueError as e:
        print(f"❌ Error with key matrix [[1,2],[3,4]]: {e}")
        print("💡 Let's try with a valid key matrix instead:")
        
        key_matrix_valid = [[1, 2], [3, 5]]  # det = 5-6 = -1 ≡ 25 (mod 26), gcd(25,26)=1
        cipher_valid = HillCipher(key_matrix_valid)
        message3 = "ATTACK AT DAWN"
        encrypted3 = cipher_valid.encrypt(message3)
        decrypted3 = cipher_valid.decrypt(encrypted3)
        
        print(f"\n📊 SUMMARY 3 (with valid key):")
        print(f"Original:  '{message3}'")
        print(f"Encrypted: '{encrypted3}'")
        print(f"Decrypted: '{decrypted3}'")


if __name__ == "__main__":
    main()
