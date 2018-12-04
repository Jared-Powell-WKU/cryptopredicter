import os, pandas as pd, json, numpy as np
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from prepare_data import prepare_data
# Set up files
dirname = os.path.dirname(__file__)
folder = os.path.join(dirname, 'coinapi/price')

if not os.path.isdir('coinapi'):
    os.makedirs('coinapi')
    os.makedirs('coinapi/price')
else:
    if not os.path.isdir('coinapi/price'):
        os.makedirs('coinapi/price')
if len(os.listdir(folder) ) < 25:
    exec(open('getPrice.py').read())

# Attempt to predict using linear regression

current = os.path.join(folder, '363.json')
with open(current) as cp:
    data = json.load(cp)

# for entry in data['data']:
#     dateMap[entry['date']] = {'price':entry['price'], 'name':data['coin']['name']}


df = pd.read_json(json.dumps(data['data']))

forecast_col = 'price'
forecast_out = 15 #how far to forecast 
test_size = 715 #size of test set

X_train, X_test, Y_train, Y_test , X_lately = prepare_data(df,forecast_col,forecast_out,test_size) #calling the method were the cross validation and data preperation is in
i = 0
total = [0] * forecast_out
while i < 10000:
    learner = linear_model.LinearRegression() #initializing linear regression model

    learner.fit(X_train,Y_train) #training the linear regression model
    score=learner.score(X_test,Y_test)#testing the linear regression model

    forecast= learner.predict(X_lately) #set that will contain the forecasted data

    response={}#creting json object
    response['test_score']=score
    response['forecast_set']=forecast
    j = 0
    for values in forecast:
        total[j] += values
        j+=1
    i+=1
    print('Completed',str(i)+' iterations of 100000')
j = 0
while j < len(total):
    total[j] /= i
    j+=1
print(total)