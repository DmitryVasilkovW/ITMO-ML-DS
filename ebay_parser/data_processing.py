import pandas as pd
from ebay_parser.utils import clean_price


def preprocess_data(df):
    df['price'] = df['price'].apply(clean_price)

    df['condition'] = df['condition'].str.lower()

    df['price_normalized'] = (df['price'] - df['price'].min()) / (df['price'].max() - df['price'].min())

    return df
