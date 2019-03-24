# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 12:59:27 2019

@author: Ryan
"""

import random
import roll_to_play

def play_half_inning():
    runs_scored = 0
    outs = 0
    strikes = 0
    
    while outs < 3:
        rolls = [random.randint(1,6), random.randint(1,6)]
        outcome = roll_to_play.rolls_to_plays(rolls)
        
        if outcome == "strike":
            strikes += 1
            if strikes >= 3:
                outs += 1
        else:
            strikes = 0
            