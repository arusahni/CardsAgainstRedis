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

    def __init__(self, conn, user):
        """Do the thing """
        self.hand = []
        self.score = 0
        self._conn = conn
        self.user = user

    def get_hand(self):
        if len(self.hand) < HAND_SIZE:
            self._draw_up()
        print("Hand has {} cards".format(len(self.hand)))

    def _draw_up(self):
        for card_text in white_cards:
            card_user = self._conn.get("white:{}".format(card_text))
            card_user = card_user.decode('utf-8')
            if card_user == self.user:
                print("Taking: {}".format(card_text))
                self.hand.append(card_text)
            else:
                print("Not taking: {}".format(card_text))
            if len(self.hand) >= HAND_SIZE:
                break
        if len(self.hand) < HAND_SIZE:
            print("!! Deck is empty.")

def play_game():
    conn = get_connection()
    user = input("User name: ")
    game = CarGame(conn, user)
    game.get_hand()
    print("Bye, {}".format(game.user))

if __name__ == "__main__":
    play_game()
