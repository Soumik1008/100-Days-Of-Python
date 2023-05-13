from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(direction,text,shift):
    new_text=" "
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = position + shift
            elif direction == "decode":
                new_position = position - shift
            new_letter = alphabet[new_position]
            new_text+=new_letter
        else:
            new_text+=letter
    print(f"The {direction}d text is{new_text}")
    
should_continue = True  
while should_continue:  
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    shift = shift % 26
    caesar(direction,text,shift)

    result = input("Type 'Yes' to continue otherwise 'No' ")
    if result == "No":
        should_continue = False
        print("Goodbye!")
    