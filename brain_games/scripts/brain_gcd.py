#!/usr/bin/env python3

from brain_games.games.brain_gcd_game import gcd_game
from brain_games.games.name_ask import tell_me


def gcd_game_script():
    print('Welcome to the Brain Games!')
    name = tell_me()
    gcd_game(name)


def main():
    gcd_game_script()


if __name__ == '__main__':
    main()
