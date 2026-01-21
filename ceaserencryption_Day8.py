alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]



def encrypt_decrypt(original_text,shift_amount,decode_or_decrypt):
        if decode_or_decrypt == "decode":
                 shift_amount *= -1
        output_text = ""
        for letter in original_text:
    
            if letter not in alphabet:
                  output_text += letter
                  continue
            original_letter = alphabet.index(letter) + shift_amount

            original_letter = original_letter % len(alphabet)

            output_text += alphabet[original_letter]

        print(f"Here is the {decode_or_decrypt}d result: {output_text} Where each of the letter of '{original_text}' is shifted up by {shift_amount}.")
    
        

        
while True:

    
    direction = input("Type 'encode' to encrypt,type 'decode' to decrypt or 1 to end: \n").lower()
    if direction == "1":
         break
             
    text = input("Type your message:\n").lower()
    shift = int(input("type the shift number:\n"))

    
    encrypt_decrypt(original_text= text, shift_amount=shift,decode_or_decrypt = direction)
        
    


