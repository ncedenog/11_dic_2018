#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:13:20 2018

@author: nataliecedeno
"""

#%%
class Product:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality
    
    
def recalculate_quality(product):
    if product.name == "potato":
        product.quality = product.quality - 0.5
    elif product.name == "cheese":
        product.quality = product.quality - 2
    else:
        if product.quality < 5:
            product.quality -= 3
            
    return product

potato = Product("potato", 9)
chesse = Product("cheese", 7)

#%%