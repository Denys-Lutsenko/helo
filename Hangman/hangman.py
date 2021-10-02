print("HANGMAN"  "\nThe game will be available soon.")
word = 'python'
print('Guess the word:')
a = input()
if a == word:
    print("You survived!")
else:
    print("You lost!")