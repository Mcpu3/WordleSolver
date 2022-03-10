from math import log2
from random import randint
from wordle import Wordle


def main():
    wordle = Wordle('words.txt')
    solver = Solver(wordle)
    solver.play()


class Solver:
    def __init__(self, wordle):
        self.wordle = wordle

    def play(self):
        while True:
            guess = self.__solve()
            print('Guess  : ' + guess)
            result = input('Result?: ')
            if result == '--exit':
                return
            if result == '00000':
                return
            _ = self.wordle.submit(guess, result)

    def __solve(self):
        if len(self.wordle.valid_corrects) > 1:
            guess = self.__calculate_guess_of_maximum_entropy()
        else:
            guess = self.wordle.valid_corrects[0]
        return guess

    def __calculate_guess_of_maximum_entropy(self):
        guesses_and_entropies = sorted([(valid_guess, self.__calculate_entropy(valid_guess)) for valid_guess in self.wordle.valid_guesses], key=lambda guess_and_entropy: guess_and_entropy[1], reverse=True)
        guess_of_maximum_entropy = guesses_and_entropies[randint(0, min(len(guesses_and_entropies) - 1, 10))][0]
        return guess_of_maximum_entropy

    def __calculate_entropy(self, guess):
        results = {}
        for valid_correct in self.wordle.valid_corrects:
            result = self.wordle.judge(guess, valid_correct)
            if result not in results:
                results[result] = 1
            else:
                results[result] += 1
        entropy = -sum([p * log2(p) for p in results.values()])
        return entropy


if __name__ == '__main__':
    main()