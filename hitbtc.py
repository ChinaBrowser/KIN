#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 FawkesPan
#
#

import requests

def GetPrice(pair='KINETH'):
    Fee = 1 - GetFee()
    url = 'https://api.hitbtc.com/api/2/public/orderbook/' + pair
    data = requests.get(url).json()
    ret = {}
    ret['ask'] = float(data['ask'][0]['price']/Fee)
    ret['askamount'] = int(data['ask'][0]['size'])
    ret['bid'] = float(data['bid'][0]['price']*Fee)
    ret['bidamount'] = int(data['bid'][0]['size'])
    return ret

def GetFee():
    return 0.001