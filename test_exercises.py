#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:17:58 2018

@author: nataliecedeno
"""

#%%

from exercises import recalculate_quality
from exercises import Product, potato, potato1, veggies, cheese

def test_recalculate_quality():
    values = [potato]
    for item in values:
        assert recalculate_quality(item).quality == 3.5
        
def test_recalculate_quality1():
    values = [cheese]
    for item in values:
        assert recalculate_quality(item).quality == 3

def test_recalculate_quality2():
    values = [veggies]
    for item in values:
        assert recalculate_quality(item).quality == 0
        
def test_recalculate_quality3():
    values = [potato1]
    for item in values:
        assert recalculate_quality(item).quality == 1
    

        
#%%