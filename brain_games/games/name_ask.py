import prompt


def tell_me():
    name = prompt.string('May I have your name? ')
    if name != '':
        print(f'Hello, {name}!')
        return name
