#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 16:21:05 2018

@author: nataliecedeno
"""

#%%
import requests


def take_all_repository(user):

    url = "https://api.github.com/users/{}/repos".format(user)
    response = requests.get(url).json()
    
    return response
    
take_all_repository("ncedenog")


#%%
import requests


def description_repository(user):

    url = "https://api.github.com/users/{}/repos".format(user)
    response = requests.get(url).json()
    
    description_lst ={}
    
    
    for i in response:
        
        description_lst.update({"Name":i["name"]})
        description_lst.update({"Number of stars":i["stargazers_count"]})
        description_lst.update({"Language":i["language"]})
        description_lst.update({"Url":i["url"]})
        
        print ([description_lst])




#    
description_repository("ncedenog")
#%%