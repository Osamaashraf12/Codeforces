n = int(input(''))
for i in range(n):
    word = input("")
    if len(word) > 10:
        modified_word = f'{word[0]}{len(word)-2}{word[-1]}'
        print(modified_word)
    else:
        print(word)
