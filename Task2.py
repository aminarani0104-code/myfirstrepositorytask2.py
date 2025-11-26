def caesar_cipher():
    print("\n Enter the plain text:", end="")
    plain = input()
    
    while True:
        try:
            print("\n Enter the key value:", end="")
            key = int(input())
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the key.")

    # --- ENCRYPTION ---
    cipher = ""
    for char in plain:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            
            if 'a' <= char <= 'z':
                start_char_ascii = ord('a')
            else:
                start_char_ascii = ord('A')
            
            char_index = ord(char) - start_char_ascii
            new_index = (char_index + key) % 26
            new_char = chr(start_char_ascii + new_index)
            cipher += new_char
        else:
            cipher += char

    print("\n\n ENCRYPTED TEXT: %s" % cipher)

    # --- DECRYPTION ---
    decrypted_plain = ""
    for char in cipher:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            if 'a' <= char <= 'z':
