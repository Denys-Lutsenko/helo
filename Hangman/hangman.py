import random
print("HANGMAN"  "\nThe game will be available soon.")
the_words = ['python', 'java', 'javascript', 'php']
word = the_words[random.randrange(4)]
#print('answer', word)
print('Guess the word:')
a = input()
if a == word:
    print("You survived!")
else:
    print("You lost!")