import os

dirname = os.path.dirname(__file__)
filenameMC = os.path.join(dirname, 'coinapi/marketCap')
filenameP = os.path.join(dirname, 'coinapi/price')

if not os.path.isdir('coinapi'):
    os.makedirs('coinapi')
    os.makedirs('coinapi/marketCap')
    os.makedirs('coinapi/price')
else:
    if not os.path.isdir('coinapi/marketCap'):
        os.makedirs('coinapi/marketCap')
    if not os.path.isdir('coinapi/price'):
        os.makedirs('coinapi/price')
if len(os.listdir(filenameMC) ) < 25:
    execfile('getmarketCap.py')
if len(os.listdir(filenameP) ) < 25:
    execfile('getPrice.py')
