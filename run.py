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
import requests

REFRESH_DELAY = 10
TG_BOT_ENABLE = False
TG_BOT_KEY = ''
TG_CHAT_ID = 0
MIN_DIFF = 3

URL = 'https://api.telegram.org/bot%s/sendMessage' % TG_BOT_KEY
PARAM = {}
PARAM['chat_id'] = TG_CHAT_ID

HITFee = 1 - hitbtc.GetFee()
COSSFee = 1 - coss.GetFee()
STRFee = 1 - stellar.GetFee()

def TGSend(message):
    if TG_BOT_ENABLE == False:
        return
    try:
        PARAM['text'] = message
        res = requests.post(URL, data = PARAM)
        return
    except IOError as e:
        print(e)
        return

while True:
    try:
        HIT = hitbtc.GetPrice()
        COSS = coss.GetPrice()
        STR = stellar.GetPrice()
        TIME = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if HIT['bid'] > COSS['ask']:
            rate = (HIT['bid']*HITFee*COSSFee/COSS['ask']-1)*100
            print(TIME + '    COSSIO Buy | HitBTC Sell ' + str(rate) + '%')
        if HIT['bid'] > STR['ask']:
            rate = (HIT['bid']/STR['ask']-1)*100
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
    except IOError as e:
        print(e)
        time.sleep(15)
