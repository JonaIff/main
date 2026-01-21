import random

hangman_list = [
    "Quarantäne",
    "Rhabarber",
    "Chrysantheme",
    "Jalousie",
    "Boulevard",
    "Delikatessen",
    "Majonäse",
    "Akklimatisation",
    "Psychiatrie",
    "Symptomatik",
    "Kontroverse",
    "Subvention",
    "Desillusionierung",
    "Parallelogramm",
    "Meteorologie",
    "Kataklysmus",
    "Silhouette",
    "Portemonnaie",
    "Thermodynamik",
    "Schmetterlingsflügel",
    "Schifffahrtsgesellschaft",
    "Zugvogelwanderung",
    "Röntgenstrahlung",
    "Philanthrop",
    "Akustikgitarre",
    "Mikroorganismus",
    "Amphibienfahrzeug",
    "Wasserstoffperoxid",
    "Unabhängigkeitserklärung",
    "Zirkulationssystem",
    "Inkompatibilität",
    "Rückversicherung",
    "Transzendentalismus",
    "Röntgenapparat",
    "Elektrolyse",
    "Misanthropie",
    "Polyethylenterephthalat",
    "Magnetresonanztomographie",
    "Donaudampfschifffahrtsgesellschaftskapitän",
    "Räucherlachsbrötchen",
    "Schokoladentrüffel",
    "Objektivismus",
    "Palindrom",
    "Konversationslexikon",
    "Insubordination",
    "Trivialität",
    "Synchronisation",
    "Kaleidoskop",
    "Zentrifugalkraft",
    "Überraschungsmoment",
    "Pseudonym"
]

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']






chosen_word = random.choice(hangman_list).lower()

print(chosen_word)


correct_letters = []

used_letters = []

display = ""

for position in range(len(chosen_word)):
    display += "_"
print(display)

game_over = False

lives = 7


while not game_over:
    placeholder = ""
    
    

    guess = input("----Bitte wähle einen Buchstaben: ").lower()

    used_letters.append(guess)

    for letter in chosen_word:

        if letter == guess:
            placeholder += letter
            correct_letters.append(guess)

        elif letter in used_letters:
            placeholder += letter
        
        else:
            placeholder += "_"


    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lose")
            

    if "_" not in placeholder:
        game_over = True
        print("you win")

    
    print(used_letters)
    print(placeholder)

     

   

    
    

