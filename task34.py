vowels_ru = ['у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю', 'ё']

poem = input("Введите стих. Разделяя фразы пробелами: ")

def is_rhythm_ru(poem, vowels = vowels_ru):
    poem = poem.split()  
    syllables = []
    for stanza in poem:
        syllables.append(sum(letter in vowels for letter in stanza)) 
    if len(set(syllables)) == 1:
        return True
    return False

def answer(question, answer_true, answer_false):
    if question:
        return answer_true
    return answer_false

print(answer(is_rhythm_ru(poem), "Парам пам-пам", "Пам парам"))