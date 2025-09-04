import mysql.connector
import random
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your_password',
    database='word_game'
)
cursor =conn.cursor()
cursor.execute("SELECT word FROM words")
word_list =[row[0].lower() for row in cursor.fetchall()]
secret_word =random.choice(word_list)
guessed= ['_' for _ in secret_word]
used_letters=set()
chances=5
print("\nWelcome to the Word Guess Game!")
print("Guess the word by entering one letter at a time.")
print(f"You have {chances} wrong attempts. Good luck!\n")
while chances > 0 and '_' in guessed:
    print("Word: ", ' '.join(guessed))
    print(f"Used Letters: {','.join(sorted(used_letters))}")
    guess = input("Enter a letter: ").lower()
    if not guess.isalpha() or len(guess)!=1:
        print("Enter a single alphabet only!\n")
        continue
    if guess in used_letters:
        print("Already used that letter!\n")
        continue
    used_letters.add(guess)
    if guess in secret_word:
        for idx, char in enumerate(secret_word):
            if char == guess:
                guessed[idx] = guess
        print("Good guess!\n")
    else:
        chances -= 1
        print(f"Wrong guess! {chances} chances left.\n")
if '_' not in guessed:
    print("\nCongratulations! You guessed the word:",secret_word)
else:
    print("\nDefeated! The word was:",secret_word)
cursor.close()
conn.close()
