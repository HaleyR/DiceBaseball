# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:07:20 2019

@author: Ryan
"""

class BaseObject:
    def __init__(self):
        self.first = False
        self.second = False
        self.third = False
        
        
    def update_base(self, play):
        outs = 0
        runs = 0
        
        if play == "single":
            if self.third == True:
                runs += 1
                self.third = False
            if self.second == True:
                runs += 1
                self.second = False
            if self.first == True:
                self.second = True
                self.first = False
            self.first = True
            
        elif play == "double":
            if self.third == True:
                runs += 1
                self.third = False
            if self.second == True:
                runs += 1
                self.second = False
            if self.first == True:
                self.third = True
                self.first = False
            self.second = True
            
        elif play == "base_on_error":
            if self.third == True:
                runs += 1
                self.third = False
            if self.second == True:
                self.third = True
                self.second = False
            if self.first == True:
                self.second = True
                self.first = False
            self.first = True
                
        elif play == "base_on_balls":
            if self.first == True:
                if self.second == True:
                    if self.third == True:
                        runs += 1
                    else:
                        self.third = True
                else:
                    self.second = True
            else:
                self.first = True
                
        elif play == "foul_out":
            outs += 1
            
        elif play == "out_at_first":
            if self.third == True:
                runs += 1
                self.third = False
            if self.second == True:
                self.third = False
                self.second = False
            if self.first == True:
                self.second = True
                self.first = False
            outs += 1
            
        elif play == "flyout":
            if self.third == True:
                runs += 1
                self.third = False
            outs += 1
            
        elif play == "double_play":
            if self.first == True:
                