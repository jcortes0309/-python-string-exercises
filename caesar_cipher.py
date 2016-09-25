key = "abcdefghijklmnopqrstuvwxyz" # cypher key

def encrypt(message):
    result = ""

    for letter in message:
        if letter == " ":
            result += " "
        else:
            i = (key.index(letter) + n) % len(key)
            result += key[i]

    print "Your encrypted message is: %s\n" % result

def decrypt(message):
    result = ""
    for letter in message:
        if letter == " ":
            result += " "
        else:
            i = (key.index(letter) - n) % len(key)
            result += key[i]

    print "Your decrypted message is: %s\n" % result

e_or_d = str(raw_input("\nEncrypt or decrypt a message? - Type encrypt(e) or decrypt(d): ")).lower()
if e_or_d == "encrypt" or e_or_d == "e":
    message = str(raw_input("Input message to encrypt: ")).lower()
    n = int(raw_input("How many places to shift your message? ")) # n is the spaces to shift
    encrypt(message)
elif e_or_d == "d" or e_or_d == "d":
    message = str(raw_input("Input message to decrypt: ")).lower()
    n = int(raw_input("How many places to shift your message? ")) # n is the spaces to shift
    decrypt(message)
else:
    print "\nI don't understand what you mean. Try again later!\n"
