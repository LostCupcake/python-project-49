#!/usr/bin/env python3


from brain_games.games.game_calc import calc_game
from brain_games.games.name_ask import tell_me


def calc_game_script():
    print('Welcome to the Brain Games!')
    name = tell_me()
    calc_game(name)


def main():
    calc_game_script()


if __name__ == '__main__':
    main()
