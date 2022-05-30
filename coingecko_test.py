#!/bin/python

import json
import sys
import os
import datetime
import pycoingecko
import io
from io import StringIO

try:
    cg = pycoingecko.CoinGeckoAPI()

    if len(sys.argv) != 1:
        config = json.load(open(sys.argv[1]))
    else:
        config = json.load(open("config-gecko.json"))


    today = datetime.date.today()

    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    print(today)
    today2 = new_stdout.getvalue()

    sys.stdout = old_stdout

    print(today2)

    suma = 0
    dict = {}
    for i in config.keys():
        waluta = cg.get_coin_by_id(i)['symbol']
        cena = round(cg.get_price(ids=i, vs_currencies='pln')[i]['pln'],2)
        ilosc = config[i]
        wartosc = float(ilosc) * float(cena)
        suma += wartosc
        dict[str(waluta)]=[str(cena), str(ilosc), str("{0:>9.2f}".format(wartosc))]
        
    newdict = sorted(dict.items(), key=lambda item: item[1][2])    

    os.chdir('c:/dane/btc/crypto-calc-master/log')
    plik = open(today2[:-1] + '.log','w')
    plik.write(today2)

    for i in newdict:
        print(i[0] + ' \t- ' + i[1][0] + ' * ' + i[1][1] + ' \t= ' + i[1][2])
        plik.write(i[0] + ' \t- ' + i[1][0] + ' * ' + i[1][1] + ' \t= ' + i[1][2])
        plik.write('\n')

    print('----------- Suma ----------\t= ' + str("{0:>9.2f}".format(suma)))
    plik.write('----------- Suma ----------\t= ' + str("{0:>9.2f}".format(suma)))

    plik.close()
    
except:
    os.environ['https_proxy']=''
    if len(sys.argv) != 1:
        config = json.load(open(sys.argv[1]))
    else:
        config = json.load(open("config-gecko.json"))


    today = datetime.date.today()

    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    print(today)
    today2 = new_stdout.getvalue()

    sys.stdout = old_stdout

    print(today2)

    suma = 0
    dict = {}
    for i in config.keys():
        waluta = cg.get_coin_by_id(i)['symbol']
        cena = round(cg.get_price(ids=i, vs_currencies='pln')[i]['pln'],2)
        ilosc = config[i]
        wartosc = float(ilosc) * float(cena)
        suma += wartosc
        dict[str(waluta)]=[str(cena), str(ilosc), str("{0:>9.2f}".format(wartosc))]
        
    newdict = sorted(dict.items(), key=lambda item: item[1][2])    

    os.chdir('c:/dane/btc/crypto-calc-master/log')
    plik = open(today2[:-1] + '.log','w')
    plik.write(today2)

    for i in newdict:
        print(i[0] + ' \t- ' + i[1][0] + ' * ' + i[1][1] + ' \t= ' + i[1][2])
        plik.write(i[0] + ' \t- ' + i[1][0] + ' * ' + i[1][1] + ' \t= ' + i[1][2])
        plik.write('\n')

    print('----------- Suma ----------\t= ' + str("{0:>9.2f}".format(suma)))
    plik.write('----------- Suma ----------\t= ' + str("{0:>9.2f}".format(suma)))

    plik.close()