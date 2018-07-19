#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 FawkesPan
#
#

import requests
import hitbtc

def GetPrice():
    data = requests.get('https://horizon.stellar.org/order_book?selling_asset_type=credit_alphanum4&selling_asset_code=KIN&selling_asset_issuer=GBDEVU63Y6NTHJQQZIKVTC23NWLQVP3WJ2RI2OTSJTNYOIGICST6DUXR&buying_asset_type=native').json()
    hit = hitbtc.GetPrice('XLMETH')
    ret = {}
    ret['ask'] = float(float(data['asks'][0]['price'])*hit['bid'])
    ret['askamount'] = int(float(data['asks'][0]['amount'])/float(data['asks'][0]['price']))
    ret['bid'] = float(float(data['bids'][0]['price'])*hit['ask'])
    ret['bidamount'] = int(float(data['bids'][0]['amount'])/float(data['bids'][0]['price']))
    return ret

def GetFee():
    return 0