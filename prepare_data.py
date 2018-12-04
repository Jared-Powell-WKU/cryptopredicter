import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

def prepare_data(df,forecast_col,forecast_out,test_size):
    label = df[forecast_col].shift(-forecast_out)
    X = np.array(df[[forecast_col]]) 
    X = preprocessing.scale(X) 
    X_lately = X[-forecast_out:] 
    X = X[:-forecast_out] 
    label.dropna(inplace=True) 
    y = np.array(label) 
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=test_size)

    response = [X_train,X_test , Y_train, Y_test , X_lately]
    return response
