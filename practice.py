words = ['apple', 'mango', 'banana']

                                                           #import random module
import random
def get_word(words):                                       #calling a function to get a word in uppercase randomly
    word = random.choice(words)
    return word.upper()

def hangman():                                             #making sets of used letters, word letters and setting a word randomly from get_word function
    word = get_word(words)
    word_letter = set(word)
    used_letter = []
    guessed = False                                        #number of tries is 6
    lives = 6
    print("lets play hangman!")


    while not guessed and lives > 0 and len(word_letter) > 0:        #making a while loop to loop through the code again and again till the word is fully guessed

        word_list = [letter if letter in used_letter else "_" for letter in word]    # making a list that replaces every letter in word by a '_' and if the letter is correctly guessed it is replaced
        print("\nyou have", lives, "lives left and you have used the letters", " ".join(used_letter))
        print("\nthe current word is", " ".join(word_list))
        guess = input("enter your guess: ").upper()                  #asking the user to input the guess letter

        if guess not in used_letter:                                  #making conditional statements to get a suitable output of the user guess
            used_letter.append(guess)
            if guess in word_letter:
                word_letter.remove(guess)
            else:
                lives -= 1
                print("the guess does not belong to the word")
        elif guess in used_letter:
            print("you have already used this letter before!")
        else:
            print("invalid letter")
    if lives == 0:                                                   #if the user runs out of tries he loses or else he wins
        print("\nsorry you lost hangman")
    else:
        print("\nyay you won hangman!! and the correct word was" , word)


if __name__ == "__main__":
    hangman()


