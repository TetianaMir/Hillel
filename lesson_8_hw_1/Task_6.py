import random

text = " За результатом дослідження одного англійського університету, не має значення, в якому порядку розшташовані літеру у слові. Головне, щоб перша та остання літери були на своєму місці. Решта літер можуть слідувати в абсолютно випадковому порядку, все одно текст читатиметься без проблем. Причиною цього є те, що ми читаємо не кожну букву окремо, а усе слово разом"


# first checker
def get_first_and_last_symbols(word: str):
    if len(word) > 3:
        return word[0], word[len(word) - 1], word[1:len(word) - 1]
    else:
        return word


# second checker
def get_third_symbols_and_shuffle(word: str):
    new_str = ''
    if len(word) >= 3:
        to_shuffle = [word[i:i + 2] for i in range(0, len(word), 2)]
        random.shuffle(to_shuffle)
        for three_letters in to_shuffle:
            new_str += three_letters
    else:
        new_str = word
    return new_str


def pemrtuate(text: str):
    temporary_array = text.split()
    word_array = []
    for word in temporary_array:
        if word.__contains__(","):
            word_array.append(word.replace(",", ' ').rstrip())
        elif word.__contains__("."):
            word_array.append(word.replace(".", ' ').rstrip())
        else:
            word_array.append(word)
    result_array = []
    for word in word_array:
        if len(word) >= 3:
            first_last_addition_symbols = get_first_and_last_symbols(word)
            first_symbol = first_last_addition_symbols[0]
            last_symbol = first_last_addition_symbols[1]
            additional_symbols = first_last_addition_symbols[2]
            main_text = get_third_symbols_and_shuffle(additional_symbols)
            result_array.append(first_symbol + main_text + last_symbol)
        else:
            result_array.append(word)
    return result_array


def main():
    print(pemrtuate(text))


if __name__ == '__main__':
    main()
