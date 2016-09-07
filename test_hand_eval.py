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

#def test_find_suits():
#    pair_hand = [Card('9', '♦'), Card('9', '♥'), Card('4', '♠'), Card('J', '♠'), Card('Q', '♠')]
#    assert find_suits(pair_hand) == ['♦', '♥', '♠', '♠','♠']

def test_find_pairs():
    pairs = ['8','K', 'K', 'J', '4']
    two_pairs = ['8', '8', 'K', 'K', 'J']
    pairs_set = set()
    two_pairs_set = set()
    for card in pairs:
        if pairs.count(card) == 2:
            pairs_set.add(card)
#    assert find_pairs(pairs) == ['8', 'K', 'K', '4', 'J']
    assert len(pairs_set) == 1
    for card in two_pairs:
        if two_pairs.count(card) == 2:
            two_pairs_set.add(card)
    assert len(two_pairs_set) == 2

def test_find_set():
    three_kind = [Card('K', '♦'), Card('K', '♥'), Card('K', '♠'), Card('J', '♠'), Card('4', '♠')]
    assert find_set(['K', 'K', 'K', 'J', '4']) == True

def test_find_four():
    four_kind = [Card('K', '♦'), Card('K', '♥'), Card('K', '♠'), Card('K', '♣'), Card('4', '♠')]
    assert find_four(['K', 'K', 'K', 'K', '4']) == True

def test_find_fullhouse():
    fullhouse_hand = ['K', 'K', 'K', '4', '4']
    assert find_fullhouse(fullhouse_hand) == True

def test_find_flush():
    suits = [Card('9', '♠'), Card('2', '♠'), Card('4', '♠'), Card('J', '♠'), Card('Q', '♠')]
    assert find_flush(['♠', '♠', '♠', '♠','♠']) == True

def test_strait():
    strait_kind = [Card('J', '♦'), Card('10', '♦'), Card('A', '♦'), Card('Q', '♦'), Card('K', '♦')]
    assert find_strait(['J', '10', 'A', 'Q', 'K']) == True

def test_straitFlush():
    ranks = ['J', '10', 'A', 'K', 'Q']
    suits = ['♦', '♦', '♦', '♦', '♦']
    assert find_straitFlush(ranks, suits) == True

'''def test_ranks():
    ranks_kind = [('J', '11'), ('Q', '12'), ('K', '13'), ('A', '14')]
    assert ranks(['11', '12', '13', '14']) == True'''

