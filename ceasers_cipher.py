alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Below is the encrypt function
def encrypt(text_input, shift_input):
    cipher_letter = ""
    for i in range(0, len(text_input)): # Will iterate the length of the text input
        
        alpha_len = len(alphabet)
        text_index = alphabet.index(text_input[i]) # Gets the index of each letter from the alphabet
        text_letter = alphabet[text_index] # Get specific letter in index in alphabet variable
        shift_total = text_index + shift_input
        dist_to_end = (len(alphabet) - 1) - text_index # The distance to the end of the length of the alphabet
        remain_shift = -(dist_to_end - shift_input) # The remainder left to shift after reaching the end of the alphabet
        
        if shift_total > alpha_len-1: # If the shift total is greater than the alphabet length
            cipher_letter += alphabet[remain_shift-1]# Starts from the begining with the shift input
            #print(f"IF: Index value {text_index} and letter {text_letter}")
        else:
            cipher_letter += alphabet[shift_total]
            #print(f"ELSE: Index value {text_index} and letter {text_letter}")
    
    print(cipher_letter)
    #print(dist_to_end)
    #print(remain_shift)

# Below is the decrypt function
def decrypt(dtext_input, dshift_input):
    dcipher_letter = ""
    for i in range(0, len(dtext_input)): # Will iterate the length of the text input
        
        dalpha_len = len(alphabet)
        dtext_index = alphabet.index(dtext_input[i]) # Gets the index of each letter from the alphabet
        dtext_letter = alphabet[dtext_index] # Get specific letter in index in alphabet variable
        dshift_total = dtext_index - dshift_input
        dist_to_begining =  dtext_index - 0 # The distance to the end of the length of the alphabet
        remain_shift = dist_to_begining - dshift_input # The remainder left to shift after reaching the end of the alphabet

        if dshift_total < 0: # If the shift total is greater than the alphabet length
            dcipher_letter += alphabet[remain_shift]# Starts from the begining with the shift input
            #print(f"IF: Index value {dtext_index} and letter {dtext_letter}")
        else:
            dcipher_letter += alphabet[dshift_total]
            #print(f"ELSE: Index value {dtext_index} and letter {dtext_letter}")

    print(dcipher_letter)

#decrypt(dtext_input = 'ekxknkbcvkqp', dshift_input = 2 ) # Call the function to test
#encrypt(text_input = 'civilization', shift_input = 2)   # Call the function to test

if direction == 'encode':
    encrypt(text_input = text, shift_input = shift) # Call the function
elif direction == 'decode':
    decrypt(dtext_input = text, dshift_input = shift)

