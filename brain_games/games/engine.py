import prompt


def core(question, correct_answer, name):
    for _ in range(3):
        print(f'Question: {question()}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer():
            print('Correct!')
            continue
        else:
            print(f'''
  '{answer}' is wrong answer ;(. Correct answer was '{correct_answer()}'.
  Let's try again, {name}!
  ''')
            return core(question, correct_answer, name)
    print(f'Congratulations, {name}!')
