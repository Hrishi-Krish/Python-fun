from words import words
import random

word = random.choice(words)
while len(word) < 6:
    word = random.choice(words)

word = word.upper()
guess = '-' * len(word)
attempts = 10
wordSet = set(word)
guessSet = set()
while attempts > 0 and guess != word:
    lu = ' '.join(list(guessSet))
    try:
        l = input(f"{guess} \t Remaining Attempts = {attempts} \t Letters used: {lu} \n")[0].upper()
    except:
        continue
    while l in guessSet:
        l = input(f"\nLetter already entered try again: ")[0].upper()
    if l in wordSet and l not in guessSet:
        for x in range(len(word)):
            if word[x] == l:
                guess = guess[:x] + l + guess[x+1:]
    else:
        attempts-=1
    guessSet.add(l)

if guess == word:
    print(f"Conratulations you have found {word} in {10-attempts} tries!")
else:
    print(f"YOU LOSE!.. The word was {word}")

    