vowels_ru = ['у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю']

poem = input("Введите стих. Разделяя фразы пробелами: ")
answer_true = "Парам пам-пам"
answer_false = "Пам парам"

def is_rhythm_ru(poem, vowels = vowels_ru):
    poem = poem.split()  
    syllables = []
    for stanza in poem:
        count = 0
        for letter in stanza:
            count += letter in vowels
        syllables.append(count) 
    if len(set(syllables)) == 1:
        return True
    return False

def message(key, answer_true, answer_false):
    if key:
        return answer_true
    return answer_false

print(message(is_rhythm_ru(poem), answer_true, answer_false))