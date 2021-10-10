import random
"""слов минимум 6
de=len(x)
exit()
не прави буква
повторы 
не прав + повтор+несколько букв+ не символ а цифра 
"""
print("HANGMAN"  "\nThe game will be available soon.")
the_words = ['python', 'java', 'javascript', 'php']
word = random.choice(the_words)
print(word[0:len(word)-3]+"---")
inputChar = input()
if inputChar in word:
    print("You survived!")
else:
    print("You lost!")