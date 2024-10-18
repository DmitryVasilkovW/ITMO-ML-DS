import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

from ebay_parser.utils import convert_utils


def numeric_normalize(df):
    numeric_cols = ['rating', 'reviews', 'Screen Size in', 'Storage Capacity GB', 'RAM GB', 'Camera Resolution MP']
    numeric_cols = [col for col in numeric_cols if col in df.columns]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    if numeric_cols:
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        scaler = MinMaxScaler()
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])


def categorical_normalize(df):
    categorical_cols = ['title', 'Features', 'Brand', 'Model', 'Processor', 'Chipset Model',
                        'Lock Status', 'Network', 'Operating System', 'Connectivity']
    categorical_cols = [col for col in categorical_cols if col in df.columns]

    if categorical_cols:
        df[categorical_cols] = df[categorical_cols].fillna('Unknown')

    label_encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le


def match_condition(value, condition_dict):
    for key, substrings in condition_dict.items():
        if any(substring.lower() in str(value).lower() for substring in substrings):
            return key
    return 'Unknown'


def one_hot_normalize(df):
    one_hot_cols = ['Colour', 'product condition']

    product_condition_values = convert_utils.product_condition_values
    colour_values = convert_utils.colour_values

    if 'product condition' in df.columns:
        df['product condition'] = df['product condition'].apply(lambda x: match_condition(x, product_condition_values))

    if 'Colour' in df.columns:
        df['Colour'] = df['Colour'].apply(lambda x: match_condition(x, colour_values))

    return pd.get_dummies(df, columns=one_hot_cols, prefix=one_hot_cols)


def normalize_df():
    df = pd.read_csv('../../data/ebay_smartphones_data.tsv', sep='\t')

    numeric_normalize(df)
    categorical_normalize(df)
    df = one_hot_normalize(df)

    df.to_csv('../../data/ebay_smartphones_data.csv', index=False)


normalize_df()
