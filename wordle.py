import random


def main(file):
    wordle = Wordle(file)
    test(wordle)

def test(wordle):
    while True:
        guess = input('Guess?: ')
        if guess == '--exit':
            return
        result = wordle.submit(guess)
        print('Result: ' + result)
        if result == '00000':
            return


class Wordle:
    def __init__(self, file):
        self.words = self.__load_words(file)
        self.correct = self.__choose_correct()
        self.valid_corrects = self.words
        self.valid_guesses = self.words

    def submit(self, guess, result=None):
        if result == None:
            result = self.judge(guess)
        self.__update_valid_corrects(guess, result)
        self.__update_valid_guesses(guess)
        return result

    def judge(self, guess, correct=None):
        if correct == None:
            correct = self.correct
        result = ''
        for g, c in zip(guess, correct):
            if g in correct:
                if g == c:
                    result += '0'
                else:
                    result += '1'
            else:
                result += '2'
        return result

    def __load_words(self, file):
        words = []
        with open(file) as f:
            words_raw = f.readlines()
        for word_raw in words_raw:
            word = word_raw[:-1]
            words.append(word)
        return words

    def __choose_correct(self):
        correct = random.choice(self.words)
        return correct

    def __update_valid_corrects(self, guess, result):
        valid_corrects = []
        for valid_correct in self.valid_corrects:
            if self.judge(guess, valid_correct) == result:
                valid_corrects.append(valid_correct)
        self.valid_corrects = valid_corrects

    def __update_valid_guesses(self, guess):
        valid_guesses = []
        for valid_guess in self.valid_guesses:
            if valid_guess == guess:
                continue
            valid_guesses.append(valid_guess)
        self.valid_guesses = valid_guesses


if __name__ == '__main__':
    main('words.txt')