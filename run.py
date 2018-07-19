#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 FawkesPan
#
#

import hitbtc
import coss
import stellar
import time
import datetime

REFRESH_DELAY = 5

HITFee = hitbtc.GetFee()
COSSFee = coss.GetFee()
STRFee = stellar.GetFee()

while True:
    try:
        HIT = hitbtc.GetPrice()
        COSS = coss.GetPrice()
        STR = stellar.GetPrice()
        TIME = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if HIT['bid'] > COSS['ask']:
            rate = (HIT['bid']/COSS['asks']-1)*100
            print(TIME + '    COSSIO Buy | HitBTC Sell ' + str(rate) + '%')
        if HIT['bid'] > STR['ask']:
            rate = (HIT['bid']/STR['asks']-1)*100
            print(TIME + '    Stellar Buy | HitBTC Sell ' + str(rate) + '%')
        if COSS['bid'] > HIT['ask']:
            rate = (COSS['bid']/HIT['ask']-1)*100
            print(TIME + '    HitBTC Buy | COSSIO Sell ' + str(rate) + '%')
        if COSS['bid'] > STR['ask']:
            rate = (COSS['bid']/STR['ask']-1)*100
            print(TIME + '    Stellar Buy | COSSIO Sell ' + str(rate) + '%')
        if STR['bid'] > HIT['ask']:
            rate = (STR['bid']/HIT['ask']-1)*100
            print(TIME + '    HitBTC Buy | Stellar Sell ' + str(rate) + '%')
        if STR['bid'] > COSS['ask']:
            rate = (STR['bid']/COSS['ask']-1)*100
            print(TIME + '    COSSIO Buy | Stellar Sell ' + str(rate) + '%')
        time.sleep(REFRESH_DELAY)
    except:
        time.sleep(1)