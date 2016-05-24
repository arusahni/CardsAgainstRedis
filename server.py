#!/usr/bin/env python3

import random
import redis

from cards import white_cards
from client import get_connection

class Server:
    def __init__(self, conn):
        self._conn = conn

    def step(self):
        self.check_winning_card()

    def check_winning_card(self):
        winning_card = self._conn.get('winning_card')
        if winning_card is not None:
            the_winner = self._conn.get(winning_card)
            black_card = self._conn.get('current_black_card')
            self._conn.set(black_card, the_winner)
            self.clear_hand()

    def clear_hand(self):
        self._conn.delete('winning_card')
        black_card = self._conn.set('current_black_card', '')
