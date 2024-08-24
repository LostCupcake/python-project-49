import random
from brain_games.games.engine import core


def even_loop(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    last_question = [0]

    def generate_question():
        return random.randint(1, 20)

    def question():
        last_question[0] = generate_question()
        return last_question[0]

    def correct_answer():
        return 'yes' if last_question[0] % 2 == 0 else 'no'

    core(question, correct_answer, name)
