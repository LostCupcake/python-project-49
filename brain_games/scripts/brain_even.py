#!/usr/bin/env python


import random
import prompt


name = prompt.string('May I have your name? ')
if name != '':
    print(f'Hello, {name}!')

    def even_loop():
        print('Answer "yes" if the number is even, otherwise answer "no".')
        for _ in range(3):
            number = random.randint(1, 20)
            print(f'Question: {number}')
            answer = prompt.string('Your answer: ')
            if number % 2 == 0:
                correct_answer = 'yes'
            else:
                correct_answer = 'no'
            if answer == correct_answer:
                print('Correct!')
                continue
            elif correct_answer == 'yes':
                print(f'''
'{answer}' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}!
        ''')
                return even_loop()
            else:
                print(f'''
'{answer}' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name}!
        ''')
                return even_loop()
        print(f'Congratulations, {name}!')


def main():
    even_loop()


if __name__ == '__main__':
    main()
