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

def test_find_suits():
    pair_hand = [Card('9', '♦'), Card('9', '♥'), Card('4', '♠'), Card('J', '♠'), Card('Q', '♠')]
    assert find_suits(pair_hand) == ['♦', '♥', '♠', '♠','♠']

def test_find_pairs():
    pairs = [Card('8', '♦'), Card('K', '♥'), Card('K', '♠'), Card('J', '♠'), Card('4', '♠')]
    assert find_ranks(pairs) == ['8', 'K', 'K', '4', 'J']
    assert find_len(pairs) == 2

def test_find_set():
    three_kind = [Card('K', '♦'), Card('K', '♥'), Card('K', '♠'), Card('J', '♠'), Card('4', '♠')]
    assert find_set(ranks) == ['K', 'K', 'K', 'J', '4']

def test_find_four():
    four_kind = [Card('K', '♦'), Card('K', '♥'), Card('K', '♠'), Card('K', '♣'), Card('4', '♠')]
    assert find_four(ranks) == ['K', 'K', 'K', 'K', '4']

def test_find_fullhouse():
    fullhouse_kind = [Card('K', '♦'), Card('K', '♥'), Card('K', '♠'), Card('4', '♣'), Card('4', '♠')]
    assert find_fullhouse(ranks) == ['K', 'K', 'K', '4', '4']

def test_find_flush():
    suits = [Card('9', '♠'), Card('2', '♠'), Card('4', '♠'), Card('J', '♠'), Card('Q', '♠')]
    assert find_suits(pair_hand) == ['♠', '♠', '♠', '♠','♠']

def test_strait():
    strait_kind = [Card('J', '♦'), Card('10', '♦'), Card('A', '♦'), Card('Q', '♦'), Card('K', '♦')]
    assert find_strait(['J', '10', 'A', 'Q', 'K']) == True

def test_straitFlush():
    ranks = ['J', '10', 'A', 'K', 'Q']
    suits = ['♦', '♦', '♦', '♦', '♦']
    assert find_straitFlush(ranks, suits) == True

def test_ranks():
    ranks_kind = [('J', '11'), ('Q', '12'), ('K', '13'), ('A', '14')]
    assert find_ranks[i] == [11, 12, 13, 14]

