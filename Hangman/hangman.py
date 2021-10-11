import random
"""слов минимум 6
de=len(x)
exit()
не прави буква
повторы 
не прав + повтор+несколько букв+ не символ а цифра 
"""

print("HANGMAN"  "\nThe game will be available soon.")
words = ['python', 'bask', "java", "javascript", "php"]
the_word = random.choice(words)
print("The word has", len(the_word), 'letters')
right = ['-'] * len(the_word)
wrong = []
health = 8


def update():
    for i in right:
        print(i, end='')
    print()
update()


while True:
    print('health', health)
    conjec = input("conjecture a lettre: ")
    health -= 1
    if conjec in the_word:
        index = 0
        for i in the_word:
            if i == conjec:
                right[index] = conjec
            index += 1
        update()
    else:
        if conjec not in wrong:
            wrong.append(conjec)
        else:
            print("You already conjecture that")
        print(wrong)
        if health == 0:
            print("You lost!")
            break
        #if len(wrong) > health:
        continue
    if '-' not in right:
        print("You survived!")
        print('I conject', the_word)
        break
