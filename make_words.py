import re


def main(file_of_words, file_of_words_raw):
    words = []
    with open(file_of_words_raw) as f:
        words_raw = f.readlines()
    for word_raw in words_raw:
        word = re.search('(?<=\').+(?=\')', word_raw)
        if (word == None):
            continue
        words.append(word.group(0))
    with open(file_of_words, 'w') as f:
        for word in words[:-1]:
            f.write(word + '\n')
        f.write(words[-1])

if __name__ == '__main__':
    main('words.txt', 'words_raw.txt')