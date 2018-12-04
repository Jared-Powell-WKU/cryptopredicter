import requests, json, datetime as dt, os

dirname = os.path.dirname(__file__)
folder = os.path.join(dirname, 'coinapi/')

now = dt.datetime.now()
year = str(now.year)
lastyear = str(now.year-1)
yearbeforethat = str(now.year-2)

if now.day < 10:
    day = "0"+str(now.day)
else:
    day = str(now.day)
if now.month < 10:
    month = "0"+str(now.month)
else:
    month = str(now.month)

urlpart1 = 'https://www.cryptocurrencychart.com/api/coin/history/'
urlpart2 = '/'+lastyear+'-'+month+'-'+day+'/'+year+'-'+month+'-'+day+'/price/USD'
url2part1 = 'https://www.cryptocurrencychart.com/api/coin/history/'
url2part2 = '/'+yearbeforethat+'-'+month+'-'+day+'/'+lastyear+'-'+month+'-'+day+'/price/USD'
headers = dict(
    Key="cdbb52cebef377eb7edac0a0f89142ca",
    Secret="70977d1fd58b5fca8a3be4b1697346fd"
)

with open(os.path.join(folder, 'data.json')) as d:
    coinNames = json.loads(d)
coinIDs = []
for entry in coinNames['id']:
    coinIDs.append(entry)

i = 0
while i < len(coinIDs):
    url = urlpart1+coinIDs[i]+urlpart2
    resp = requests.get(url=url, headers=headers)
    data = resp.json()
    writeTo = 'coinapi/price/'+coinIDs[i]+'.json'
    with open(writeTo, 'w') as outfile:
        json.dump(data, outfile)
    i+=1