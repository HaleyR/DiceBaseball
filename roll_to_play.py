# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def rolls_to_plays(rolls):
    rolls = rolls.sort()
    output = ""
    if rolls[0] == 1:
        if rolls[1] == 1:
            output = "double"
        elif rolls[1] < 5:
            output = "single"
        elif rolls[1] == 5:
            output = "base_on_error"
        elif rolls[1] == 6:
            output = "base_on_balls"
    elif rolls[0] == 2:
        if rolls[1] < 6:
            output = "strike"
        elif rolls[1] == 6:
            output = "foul_out"
    elif rolls[0] == 3:
        output = "out_at_first"
    elif rolls[0] == 4:
        output = "fly_out"
    elif rolls[0] == 5:
        if rolls[1] == 5:
            output = "double_play"
        elif rolls[1] == 6:
            output = "triple"
    elif rolls[0] == 6:
        output = "homerun"
        
    return output
        