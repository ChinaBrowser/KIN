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
MIN_DELAY = 600
LAST_MSG = int(time.time()) - MIN_DELAY

URL = 'https://api.telegram.org/bot%s/sendMessage' % TG_BOT_KEY
PARAM = {}
PARAM['chat_id'] = TG_CHAT_ID

is_true = False

def TGSend(message):
    if TG_BOT_ENABLE == False:
        return
    if (LAST_MSG + MIN_DELAY) >= int(time.time()):
        return
    
    is_true = True

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
            rate = (HIT['bid']/COSS['ask']-1)*100
            msg = 'KIN COSSIO Buy | HitBTC Sell ' + str(rate) + '%'
            print(TIME + '    ' + msg)
            TGSend(msg)
        if HIT['bid'] > STR['ask']:
            rate = (HIT['bid']/STR['ask']-1)*100
            msg = 'KIN Stellar Buy | HitBTC Sell ' + str(rate) + '%'
            print(TIME + '    ' + msg)
            TGSend(msg)
        if COSS['bid'] > HIT['ask']:
            rate = (COSS['bid']/HIT['ask']-1)*100
            msg = 'KIN HitBTC Buy | COSSIO Sell ' + str(rate) + '%'
            print(TIME + '    ' + msg)
            TGSend(msg)
        if COSS['bid'] > STR['ask']:
            rate = (COSS['bid']/STR['ask']-1)*100
            msg = 'KIN Stellar Buy | COSSIO Sell ' + str(rate) + '%'
            print(TIME + '    ' + msg)
            TGSend(msg)
        if STR['bid'] > HIT['ask']:
            rate = (STR['bid']/HIT['ask']-1)*100
            msg = 'KIN HitBTC Buy | Stellar Sell ' + str(rate) + '%'
            print(TIME + '    ' + msg)
            TGSend(msg)
        if STR['bid'] > COSS['ask']:
            rate = (STR['bid']/COSS['ask']-1)*100
            msg = 'KIN COSSIO Buy | Stellar Sell ' + str(rate) + '%'
            print(TIME + '    ' + msg)
            TGSend(msg)
        if is_true:
            LAST_MSG = int(time.time())
            is_true = False

        time.sleep(REFRESH_DELAY)
    except IOError as e:
        print(e)
        time.sleep(15)
