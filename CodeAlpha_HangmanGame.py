import random

def hangman():
    words = ["apple", "banana", "grape", "mango", "peach"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("🎮 Welcome to Hangman!")

    while attempts > 0:
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        print("\nWord:", display.strip())

        if "_" not in display:
            print("🎉 You guessed it right! The word was:", word)
            break

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("⚠️ You already guessed that.")
        elif guess in word:
            print("✅ Good guess!")
            guessed_letters.append(guess)
        else:
            print("❌ Wrong guess.")
            guessed_letters.append(guess)
            attempts -= 1
            print(f"Remaining attempts: {attempts}")

    else:
        print("💀 Game Over! The word was:", word)

hangman()
