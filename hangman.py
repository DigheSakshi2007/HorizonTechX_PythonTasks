import random
def play_hangman():
    words=["python","code","flask","django","react"]
    word_to_guess=random.choice(words)
    guessed_letters=[]
    incorrect_guesses=0
    max_incorrect=6
    print("---- Welcome to Hangman game !----")
    while incorrect_guesses  < max_incorrect:
        display_word=""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word+=letter+" "
            else:
                display_word+="_ "
        print("\nword: ",display_word.strip())
        if "_" not in display_word:
            print("Congratulations! You guesses the word correctly!")
            break
        guess=input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue
        guessed_letters.append(guess)
        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            remaining = max_incorrect - incorrect_guesses
            print(f"Wrong guess! Incorrect guesses left: {remaining}")
    if incorrect_guesses == max_incorrect:
        print(f"\nGame Over! The correct word was: {word_to_guess}")
if __name__ == "__main__":
    play_hangman()
