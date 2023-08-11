from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
def caeser(text, direction, shift):
    final_text=""
    for char in text:
        if char in alphabet:
            if direction=="encode":
                index = (alphabet.index(char) + shift) % 26
                final_text += alphabet[index]
            elif direction=="decode":
                index = (alphabet.index(char) - shift) % 26
                final_text += alphabet[index] 
        else:
            final_text+=char
    print("Your " + direction + "d message is:", final_text)
should_continue=True
    
while should_continue:    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))    
    caeser(text, direction, shift)  
    result=input("Type 'yes' if you want to go again or else type 'no'\n")
    if result=="no":
        should_continue=False
        print("GoodBye.. 👋")