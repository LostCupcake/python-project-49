

import operator
import random
from brain_games.games.engine import core


def calc_game(name):
    print('What is the result of the expression?')

    first_num = [0]
    second_num = [0]
    question = [0]
    return_question = [0]
    operators = ["-", "+", "*"]

    def generate_num():
        return random.randint(1, 100)

    def question_num():
        first_num[0] = generate_num()
        second_num[0] = generate_num()
        question[0] = random.choice(operators)
        return_question[0] = f'{first_num[0]} {question[0]} {second_num[0]}'
        return return_question[0]

    def correct_answer_num():
        operator_func = {'+': operator.add, '-': operator.sub,
                         '*': operator.mul}

        return str(operator_func[question[0]](first_num[0], second_num[0]))

    core(question_num, correct_answer_num, name)
