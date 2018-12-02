import requests, json 
urlpart1 = 'https://www.cryptocurrencychart.com/api/coin/history/'
urlpart2 = '/2017-12-02/2018-12-02/price/USD'
headers = dict(
    Key="REMOVED",
    Secret="REMOVED"
)
coinIDs = ["363", "365", "364", "2487", "373", "2391", "366", "390", "2796", "2779", "370", "2233", "367", "369", "2471", "368", "2463", "375", "2877", "2797", "2550", "378", "3473", "2539", "2438"]
i = 0;
while i < len(coinIDs):
    url = urlpart1+coinIDs[i]+urlpart2
    resp = requests.get(url=url, headers=headers)
    data = resp.json()
    writeTo = 'coinapi/price/'+coinIDs[i]+'.json'
    with open(writeTo, 'w') as outfile:
        json.dump(data, outfile)
    i+=1