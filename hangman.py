import random
import copy


turnCount = 8

def choose_word():
    with open('dictionary.txt', 'r') as f:

        # gets total words in file
        dictlength = copy.copy(sum(1 for line in f))

        # chooses a random number between 0 and total length  
        random_num = random.randint(0, dictlength - 1) 

        # returns to top of file
        f.seek(0)

        # copies readlines list to data list var
        data = copy.copy(f.readlines())

        # prints random word from data list
        return data[random_num].strip()

word = list(choose_word())
deadMan = {'post': {'horizontal': ('|'.ljust(5, u"\u203E")), 
                   'vertical': '|\n'},
            'head': 'O',
            'body': '|',
            'armLeft': '/',
            'armRight': '\\',
            'legLeft': '/',
            'legRight': '\\',
            'noose': '|'}

#print(deadMan['post']['horizontal'] + deadMan['noose'])
#print(deadMan['post']['vertical'])

    
def print_spaces():
    # prints spaces for each letter in word
    for i in range(len(word)):
        print("_ ", end = "")
    print("\n")

def draw_board():
    print('-----') # top line
    print('| ', end = "") # f1st line irst vertical bar 
    if turnCount < 8:
        print('O', end = "") # head
    print('\n|', end = "") # 2nd line vertical bar
    if turnCount < 6:
        print("/", end = "") # left arm
    else:
        print(" ", end = "") # space if no left arm
    if turnCount < 7:
        print("|", end = "") # torso 1/2
    else:
        print(" ", end = "") # space if no torso
    if turnCount < 5:
        print("\\", end = "") # right arm 
    print("\n| ", end = "") # 3rd line vertical bar and space
    if turnCount < 4:
        print("|", end = "") # torso 2/2
    print("\n|", end = "") # 4th line vertical bar
    if turnCount < 3:
        print("/ ", end = "") # left leg and crotch space
    else:
        print("  ", end = "") # space if no left leg and crotch space
    if turnCount < 2:
        print("\\", end = "") # right left
    if turnCount < 1:
        print("\n|DEAD", end = "") # ohnodead
    print(" ")
    

def player_turn():

    global turnCount

    guessedLetters = []
    emptyword = '_' * len(word)
    lettersInWord = list(emptyword)

    while True:
        draw_board()
        print(lettersInWord)
        print("Guess a letter.")
        turn = input()
        # check if letter is in word
        if turn in word:
            print("Letter in word!")
            for i in range(len(word)):
                # fill letter in space, print spaces
                if turn == word[i]:
                    lettersInWord[i] = word[i]
            print(lettersInWord)
            if turnCount == 0:
                print("You lost!")
                print("The word was: " + wordstr)
                break
            else:
                print("Letters guessed: " + str(guessedLetters))
                print("Guesses remaining: " + str(turnCount))

            # player can guess word
            print("Guess word: ")
            wordguess = input()

            # if the guess is right, they won
            if wordguess == (''.join(word)).strip():
                print("You won!")
                break 
            else:
                print("Wrong word!")
                turnCount = turnCount - 1
                if turnCount == 0:
                    print("You lost!")
                    print("The word was: " + wordstr)
                    break
                else:
                    print("Letters guessed: " + str(guessedLetters))
                    print("Guesses remaining: " + str(turnCount))
                    #TODO: if guess is wrong, fill in hangman and increment turncount

        # if the letter is not in the word, lose a turn and add to hangman
        else:
            print("Letter not in word")
            #TODO: fill in hangman
            turnCount = turnCount - 1
            guessedLetters.append(turn)
            print("Incorrect letters guessed: " + str(guessedLetters))
            print("Guesses remaining: " + str(turnCount))
        
        if turnCount == 0:
            print("You lost!")
            draw_board()
            print("The word was: " + str(word))
            break

            
player_turn()