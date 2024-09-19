import random
from brain_games.games.engine import core


def gcd_game(name):

    print('Find the greatest common divisor of given numbers.')
    first_number = [0]
    second_number = [0]
    return_question = [0]

    def generate_number():
        return random.randint(1, 100)

    def correct_answer_gcd():
        while first_number[0] > 0 and second_number[0] > 0:
            if first_number[0] >= second_number[0]:
                first_number[0] = first_number[0] % second_number[0]
            else:
                second_number[0] = second_number[0] % first_number[0]
        return str(max(first_number[0], second_number[0]))

    def question_gcd():
        first_number[0] = generate_number()
        second_number[0] = generate_number()
        return_question[0] = f'{first_number[0]} {second_number[0]}'
        return return_question[0]

    core(question_gcd, correct_answer_gcd, name)
