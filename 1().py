def decrypt(cip_text, k):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dec_text = ""
    
    for char in cip_text:
        if char.isalpha():
            upper = char.isupper()
            
            char_index = alphabet.index(char.upper())
            
            dec_index = (char_index - k) % 26
            
            dec_char = alphabet[dec_index]
            
            if not upper:
                dec_char = dec_char.lower()
        else:
            dec_char = char
        
        dec_text += dec_char
    
    return dec_text

if __name__ == "__main__":
    cip_text = input("Enter the ciphered text: ")
    key = int(input("Enter key: "))
    
    dec_text = decrypt(cip_text, key)
    
  
    print("This is the decrypted text:", dec_text)
