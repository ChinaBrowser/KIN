#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 FawkesPan
#
#

import requests

def GetPrice():
    data = requests.get('https://exchange.coss.io/api/integrated-market/depth/kin-eth').json()
    ret = {}
    ret['ask'] = float(data[1][0][0])
    ret['askamount'] = int(float(data[1][0][1]))
    ret['bid'] = float(data[0][0][0])
    ret['bidamount'] = int(float(data[0][0][1]))
    return ret

def GetFee():
    return 0.001