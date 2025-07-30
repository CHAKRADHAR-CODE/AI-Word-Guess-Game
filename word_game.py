import mysql.connector
import random

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your_password',
    database='word_game'
)
cursor = conn.cursor()

# Fetch all words and pick one randomly
cursor.execute("SELECT word FROM words")
word_list = [row[0].lower() for row in cursor.fetchall()]
secret_word = random.choice(word_list)

# Game setup
guessed = ['_' for _ in secret_word]
used_letters = set()
chances = 5

print("\n🎮 Welcome to the Word Guess Game!")
print("👉 Guess the word by entering one letter at a time.")
print(f"You have {chances} wrong attempts. Good luck!\n")

# Game loop
while chances > 0 and '_' in guessed:
    print("Word: ", ' '.join(guessed))
    print(f"Used Letters: {', '.join(sorted(used_letters))}")
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Enter a single alphabet only!\n")
        continue

    if guess in used_letters:
        print("❗ Already used that letter!\n")
        continue

    used_letters.add(guess)

    if guess in secret_word:
        for idx, char in enumerate(secret_word):
            if char == guess:
                guessed[idx] = guess
        print("✅ Good guess!\n")
    else:
        chances -= 1
        print(f"❌ Wrong guess! {chances} chances left.\n")

# End result
if '_' not in guessed:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n💀 Defeated! The word was:", secret_word)

# Close DB connection
cursor.close()
conn.close()
