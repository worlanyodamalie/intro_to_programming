def readplain_text(filename):
     f = open(filename,"r")
     text = f.read()
     f.close()
     return text


def write_to_file(filename, text):
    file = open(filename, "w")
    file.write(text)
    file.close()


def encrypt(key, text):    
    encrypted = ""
    for c in text:

        encrypted = encrypted +str(ord(c) + (len(key) % 127))+" "
    print(encrypted)
    return encrypted



def decrypt(key, text):    
    decrypted = ""
    text = text.split()
    for c in text:

        #decrypted = decrypted +chr(int(c) + (len(key) % 127))
         decrypted = decrypted +chr(int(c) + (len(key) % 127))
    print (decrypted)
    return decrypted


    
def encryption (filename, key):
    text = readplain_text(filename)

    #cipher_text = decrypt(key, text )
    cipher_text = encrypt(key, text )  
    cipher_text = decrypt(key, text )
    write_to_file(filename, cipher_text)

#Pass plain text file and key to encryption method
encryption('plaintext.txt','cipher_text')
