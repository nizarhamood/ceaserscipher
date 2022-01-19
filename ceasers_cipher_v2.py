alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(text_input, shift_input):
    # Below is the encrypt function
    letter = ""
    for i in range(0, len(text_input)):
        
        text_index = alphabet.index(text_input[i])
        alpha_len = len(alphabet) # Gets the index of each letter from the alphabet
        text_letter = alphabet[text_index] # Get specific letter in index in alphabet variable
        

        if direction == "encode":

            shift_total = text_index + shift_input
            dist_to_end = (len(alphabet) - 1) - text_index # The distance to the end of the length of the alphabet
            remain_shift = -(dist_to_end - shift_input) # The remainder left to shift after reaching the end of the alphabet
            
            if shift_total > alpha_len-1: # If the shift total is greater than the alphabet length
                letter += alphabet[remain_shift-1]# Starts from the begining with the shift input
                #print(f"IF: Index value {text_index} and letter {text_letter}")
            
            else:
                letter += alphabet[shift_total]
                #print(f"ELSE: Index value {text_index} and letter {text_letter}")

        elif direction == "decode":

            shift_total = text_index - shift_input
            dist_to_begining =  text_index - 0 # The distance to the end of the length of the alphabet
            remain_shift = dist_to_begining - shift_input # The remainder left to shift after reaching the end of the alphabet
            
            if shift_total < 0: # If the shift total is greater than the alphabet length
                letter += alphabet[remain_shift]# Starts from the begining with the shift input
                #print(f"IF: Index value {text_index} and letter {text_letter}")
            
            else:
                letter += alphabet[shift_total]
                #print(f"ELSE: Index value {text_index} and letter {text_letter}")

    print(letter)


ceaser(text_input = text, shift_input = shift)

