import pandas as pd
import numpy as np
from env import user, password, host
import acquire_zillow

df = acquire_zillow.get_zillow_data()

def fill_nulls(df):
    df.poolcnt = df.poolcnt.replace(np.nan, 0)
    df.hashottuborspa = df.hashottuborspa.replace(np.nan, 0)
    df.garagecarcnt = df.garagecarcnt.replace(np.nan, 0)
    df.taxamount = df.taxamount.replace(np.nan, 0)
    return df


def null_dropper(df, prop_required_column, prop_required_row):
    
    prop_null_column = 1 - prop_required_column
    
    for col in list(df.columns):
        
        null_sum = df[col].isna().sum()
        null_pct = null_sum / df.shape[0]
        
        if null_pct > prop_null_column:
            df.drop(columns=col, inplace=True)
            
    row_threshold = int(prop_required_row * df.shape[1])
    
    df.dropna(axis=0, thresh=row_threshold, inplace=True)
    
    return df


def home_age(df):
    df['age'] = 2017 - df['yearbuilt']
    df['age'].fillna(df['age'].median(), inplace=True)
    return df 



def handle_outliers(df):
    df = df[df.bathroomcnt <= 7.5]
    df = df[df.bathroomcnt >= 0.5]
    df = df[df.bedroomcnt <= 7]
    df = df[df.bedroomcnt >= 1]
    df = df[df.calculatedfinishedsquarefeet <= 7000]
    df = df[df.calculatedfinishedsquarefeet >= 500]
    df = df[df.taxvaluedollarcnt <= 2_000_000]

    return df

def convert_dtype(df):
    df['fips'] = df['fips'].astype(int)
    df['assessmentyear'] = df['assessmentyear'].astype(int)
   #df = df.astype(int)
    return df


def create_features(df):
    
    # create taxrate variable
    df['taxrate'] = df.taxamount/df.taxvaluedollarcnt*100

    # create acres variable
    df['acres'] = df.lotsizesquarefeet/43560

    # dollar per square foot-structure
    df['dollar_per_sqft'] = df.structuretaxvaluedollarcnt/df.calculatedfinishedsquarefeet

    # ratio of bathrooms to bedrooms
    #df['bath_bed_ratio'] = df.bathroomcnt/df.bedroomcnt

    return df

def rename_cols(df): #rename columns
    df = df.rename(columns = {'bedroomcnt':'bedroom', 'bathroomcnt':'bathroom', 'calculatedfinishedsquarefeet':'sqft', 'taxvaluedollarcnt':'home_value', 'yearbuilt':'year_built', 'taxamount':'tax_amount', 'poolcnt':'has_pool',
    'lotsizesquarefeet':'lot_size', 'transactiondate':'transaction_date', 'garagecarcnt':'garage', 'landtaxvaluedollarcnt':'land_tax', 'assessmentyear':'assessment_year', 'finishedsquarefeet12':'finished_sqft', 'calculatedbathnbr':'bed_bath', 'propertylandusedesc':'property_desc'})
    return df


def get_counties(df):
    county_df = pd.get_dummies(df.fips)
    # rename columns by actual county name
    county_df.columns = ['LA', 'Orange', 'Ventura']
    # concatenate the dataframe with the 3 county columns
    df_dummies = pd.concat([df, county_df], axis = 1)
    # drop regionidcounty and fips columns
    df_dummies = df_dummies.drop(columns = ['regionidcounty'])
    return df_dummies


def longitude_format(df):
    df.latitude = df.latitude / 1_000_000
    df.longitude = df.longitude / 1_000_000

    return df

def dummy_var(df):
    dummy_df = pd.get_dummies(df[['has_pool', 'garage', 'property_desc']], dummy_na=False, drop_first=True)
    df = pd.concat([df, dummy_df], axis=1)
    
    return df

def wrangle_zillow(df):
    df = fill_nulls(df)
    df = null_dropper(df, 0.75, 0.75)
    df = home_age(df)
    df = convert_dtype(df)
    df = create_features(df)
    df = handle_outliers(df)
    df = rename_cols(df)
    df = get_counties(df)
    df = longitude_format(df)
    df = dummy_var(df)
    
    return df

