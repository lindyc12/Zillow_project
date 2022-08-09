
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import SelectKBest, RFE, f_regression 
import sklearn.preprocessing
from sklearn.model_selection import train_test_split
import env
import pandas as pd


def split(df, stratify_by='logerror'):
    # split df into train_validate 
    train_validate, test = train_test_split(df, test_size=.20, random_state=13)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=13)

    X_train = train.drop(columns=['logerror'])
    y_train = train[['logerror']]

    X_validate = validate.drop(columns=['logerror'])
    y_validate = validate[['logerror']]

    X_test = test.drop(columns=['logerror'])
    y_test = test[['logerror']]

    return train, X_train, X_validate, X_test, y_train, y_validate, y_test




# scale the data
from sklearn.preprocessing import MinMaxScaler
def scaled_data(X_train, X_validate, X_test, y_train, y_validate, y_test):
    # Make the scaler
    scaler = MinMaxScaler()

    # Fit the scaler
    scaler.fit(X_train)

    # Use the scaler
    X_train_scaled = pd.DataFrame(scaler.transform(X_train), columns=X_train.columns)
    X_validate_scaled = pd.DataFrame(scaler.transform(X_validate), columns=X_train.columns)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X_train.columns)
    y_train = pd.DataFrame(y_train)
    y_validate = pd.DataFrame(y_validate)
    y_test = pd.DataFrame(y_test)
    return X_train_scaled, X_validate_scaled, X_test_scaled, y_train, y_validate, y_test


