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
cryptoValues = []
cryptoNames = []
for filename in os.listdir(folder):
    # Attempt to predict using linear regression
    current = os.path.join(folder, filename)
    with open(current) as cp:
        data = json.load(cp)
    cryptoNames.append(json.dumps(data['coin']['name']))
    df = pd.read_json(json.dumps(data['data']))

    forecast_col = 'price'
    forecast_out = 15 # How far to forecast 
    test_size = (len(data)) # Size of test set

    X_train, X_test, Y_train, Y_test , X_lately = prepare_data(df,forecast_col,forecast_out,test_size) # Prepare our data for fitting
    i = 0
    total = [0] * forecast_out
    while i < 1000:
        learner = linear_model.LinearRegression() # Initializing linear regression model

        learner.fit(X_train,Y_train) # Training the linear regression model
        score = learner.score(X_test,Y_test) # Testing the linear regression model

        forecast= learner.predict(X_lately) # Set that will contain the forecasted data

        response={}
        response['test_score']=score
        response['forecast_set']=forecast
        j = 0
        for values in forecast:
            total[j] += values
            j+=1
        i+=1
    j = 0
    while j < len(total):
        total[j] /= i
        j+=1
    cryptoValues.append(total)
    print(json.dumps(data['coin']['name'])+" is now complete.")
i = 0    
while i < len(cryptoNames):
    print(cryptoNames[i], end = ': ')
    j = 0
    while j < len(cryptoValues[i]):
        print ('Day '+str(j+1)+': '+str(cryptoValues[i][j]), end = ' ')
        j+=1
    print('\n')
    i+=1