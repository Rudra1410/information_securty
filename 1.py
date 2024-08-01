def encrypt(plaintext, k):
    # Define the alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_text = ""
    
    
    for char in plaintext:
        if char.isalpha():
            
            upper = char.isupper()
            
          
            char_index = alphabet.index(char.upper())
            

            enc_index = (char_index + k) % 26
            
            
            enc_char = alphabet[enc_index]
            
           
            if not upper:
                enc_char = enc_char.lower()
        else:
            
            enc_char = char
        
      
        encrypted_text += enc_char
    
    return encrypted_text

if __name__ == "__main__":
    
    plaintext = input("Enter plaintext: ")
    key = int(input("Enter the key (integer): "))
    
    
    encrypted_text = encrypt(plaintext, key)
    
   
    print("Encrypted Text:", encrypted_text)
