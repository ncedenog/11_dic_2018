#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:17:58 2018

@author: nataliecedeno
"""

#%%

from exercises import recalculate_quality
from exercises import Product, potato, cheese

def test_recalculate_quality():
    assert recalculate_quality(potato).quality == 8.5
        
#%%