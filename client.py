#!/usr/bin/env python3

"""A tool for great evil... and fun! (But mostly evil)."""

import random
import redis

from cards import white_cards

HAND_SIZE = 10

def get_connection(host="10.28.59.172", port=6379, db=0):
    """Get a connection

    :param host: TODO
    :param port: TODO
    :param db: TODO
    :returns: TODO

    """
    conn = redis.StrictRedis(host=host, port=port, db=db)
    return conn

class CarGame:
    """Play the game"""

    def __init__(self, conn):
        """Do the thing """
        self.hand = []
        self.score = 0
        self._conn = conn

    def get_hand(self):
        if len(self.hand) < HAND_SIZE:
            self._draw_up(HAND_SIZE - len(self.hand))
        print("Hand has {} cards".format(len(self.hand)))

    def _draw_up(self, number):
        for _ in range(number):
            card_text = random.choice(white_cards)
            card_info = self._conn.get("white:{}".format(card_text))
            card_info = card_info.decode('utf-8')
            if card_info: #taken
                print("Taken: {}".format(card_text))
            else:
                self.hand.append(card_text)
                print("Not taken: {}".format(card_text))

def play_game():
    conn = get_connection()
    game = CarGame(conn)
    game.get_hand()

if __name__ == "__main__":
    play_game()
