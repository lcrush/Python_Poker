# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 17:39:00 2016

@author: Lisa Rush
"""

from pokerdeck import *
from Poker_mid import *

def test_deal_hand():
    assert(len(deal_hand()) == 5)
    
def test_no_dupes():
    hand = deal_hand()
    for card in hand:
        assert hand.count(card) == 1

