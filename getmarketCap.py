import requests, json, datetime as dt

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
urlpart2 = '/'+lastyear+'-'+month+'-'+day+'/'+year+'-'+month+'-'+day+'/marketCap/USD'
url2part1 = 'https://www.cryptocurrencychart.com/api/coin/history/'
url2part2 = '/'+yearbeforethat+'-'+month+'-'+day+'/'+lastyear+'-'+month+'-'+day+'/marketCap/USD'
headers = dict(
    Key="cdbb52cebef377eb7edac0a0f89142ca",
    Secret="70977d1fd58b5fca8a3be4b1697346fd"
)
coinIDs = ["363", "365", "364", "2487", "373", "2391", "366", "390", "2796", "2779", "370", "2233", "367", "369", "2471", "368", "2463", "375", "2877", "2797", "2550", "378", "3473", "2539", "2438"]
i = 0
while i < len(coinIDs):
    url = urlpart1+coinIDs[i]+urlpart2
    resp = requests.get(url=url, headers=headers)
    data = resp.json()
    url2 = url2part1+coinIDs[i]+url2part2
    resp2 = requests.get(url=url2, headers=headers)
    data2 = resp2.json()
    data2['data'].extend(data['data'])
    writeTo = 'coinapi/marketCap/'+coinIDs[i]+'.json'
    with open(writeTo, 'w') as outfile:
        json.dump(data2, outfile)
    i+=1