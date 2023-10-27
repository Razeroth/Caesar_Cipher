import string

def caesar(text, key, char):
    # Tentukan fungsi untuk menggeser karakter dalam set karakter yang diberikan.
    def shift_char(char_set, k):
        return char_set[k:] + char_set[:k]

    # Terapkan pergeseran ke karakter huruf kecil dan huruf besar.
    shifted_chars = [shift_char(char_set, key) for char_set in char]
    
    #Tabel translasi untuk karakter asli dan karakter yang digeser.
    original_chars = ''.join(char)
    shifted_chars = ''.join(shifted_chars)
    table = str.maketrans(original_chars, shifted_chars)
    
    #Tabel translasi untuk mengenkripsi teks.
    return text.translate(table)

def decrypt_caesar(text, key, char):
    # Membalikkan kode enkripsi ke awal(Dekripsi)
    return caesar(text, -key, char)

plain_text = "Welcome to Caesar Cipher"
encrypted_text = caesar(plain_text, 3, [string.ascii_lowercase, string.ascii_uppercase])
decrypted_text = decrypt_caesar(encrypted_text, 3, [string.ascii_lowercase, string.ascii_uppercase])

print("Teks Asli:", plain_text)
print("Teks Terenkripsi:", encrypted_text)
print("Teks Terdekripsi:", decrypted_text)
