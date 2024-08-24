#!/usr/bin/env python3


from brain_games.games.game_even import even_loop
from brain_games.games.name_ask import tell_me


def even_game():
    print('Welcome to the Brain Games!')
    name = tell_me()
    even_loop(name)


def main():
    even_game()


if __name__ == '__main__':
    main()
