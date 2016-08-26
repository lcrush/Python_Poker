# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 17:39:00 2016

@author: Lisa Rush
"""

from pokerdeck import *
from Poker_Midterm_test import *

def test_deal_hand():
    assert(len(deal_hand()) == 5)
    
def test_no_dupes():
    hand = deal_hand()
    for card in hand:
        assert hand.count(card) == 1

# pair_hand = [Card('9', '♦'), Card('9', '♥'), Card('4', '♠'), Card('J', '♠'), Card('Q', '♠')]
# no_pair_hand = [Card('8', '♦'), Card('9', '♥'), Card('4', '♠'), Card('J', '♠'), Card('Q', '♠')]


def test_find_pairs():
    pairs = [Card('8', '♦'), Card('K', '♥'), Card('K', '♠'), Card('J', '♠'), Card('4', '♠')]
    assert find_ranks(pairs) == ['8', 'K', 'K', '4', 'J']


def test_find_set():
    three_kind = [Card('K', '♦'), Card('K', '♥'), Card('K', '♠'), Card('J', '♠'), Card('4', '♠')]
    assert find_set(ranks) == ['K', 'K', 'K', 'J', '4']