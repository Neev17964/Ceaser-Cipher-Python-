alphabet_dict = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 
    'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 
    'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 
    's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 
    'y': 25, 'z': 26
}


def left_shift_dict(input_dict, shift_by):
    keys = list(input_dict.keys())
    values = list(input_dict.values())
    
    shifted_values = values[-shift_by:] + values[:-shift_by]
    
    shifted_dict = {keys[i]: shifted_values[i] for i in range(len(keys))}
    return shifted_dict

def right_shift_dict(input_dict, shift_by):
    keys = list(input_dict.keys())
    values = list(input_dict.values())
    
    shifted_values = values[-shift_by:] + values[:-shift_by]
    
    shifted_dict = {keys[i]: shifted_values[i] for i in range(len(keys))}
    return shifted_dict


def encode():
    encode_num_list = [left_shifted_dict[letter] for letter in user_list_encode]
    # shifted_encode_num_list = encode_num_list[shift:] + encode_num_list[:shift]
    
    number_to_letter = {value: key for key, value in alphabet_dict.items()}

    encode_letter_list = [number_to_letter[letter] for letter in encode_num_list]

    encode = ''.join(encode_letter_list)
    print(encode)

def decode():

    decode_num_list = [new_shift_dict[letter] for letter in user_list_decode]

    number_to_letter = {value: key for key, value in right_shifted_dict.items()}
   
    decode_letter_list = [number_to_letter[letter] for letter in decode_num_list]
 
    decode = ''.join(decode_letter_list)
    print(decode)


while True: 
    user = input("Do you to encode or decode? ")
    if user == 'encode':

        user_encode = input("Enter the sentence/word you need to convert it in a code: ")
        shift = int(input("What should be the shift: "))
        
        left_shifted_dict = left_shift_dict(alphabet_dict, shift)
        user_list_encode = list(user_encode)
        
        encode()

    elif user == 'decode':
        user_decode = input("Enter the code to decode: ")
        shift = int(input("What was the shift: "))
        
        new_shift_dict = left_shift_dict(alphabet_dict, shift)
        right_shifted_dict = right_shift_dict(new_shift_dict, shift)
        user_list_decode = list(user_decode)

        decode()
    else:
        print("Spelling was not correct")
    
    last = input("Do you want to do it again or not?: (YES/NO) \n")
    if last == 'yes':
        True
    elif last == 'no':
        break
    else:
        print("Write only yes or no, nothing else")

print("PROGRAM EXITED")