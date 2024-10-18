import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler


def normalize_df():
    df = pd.read_csv('../../data/ebay_smartphones_data.tsv', sep='\t')

    numeric_cols = ['rating', 'reviews', 'Screen Size in', 'Storage Capacity GB', 'RAM GB',
                    'Camera Resolution MP']
    numeric_cols = [col for col in numeric_cols if col in df.columns]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    if numeric_cols:
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    categorical_cols = ['title', 'product condition', 'Features', 'Brand', 'Model', 'Processor', 'Chipset Model',
                        'Colour',
                        'Lock Status', 'Network', 'Operating System', 'Connectivity']
    categorical_cols = [col for col in categorical_cols if col in df.columns]

    if categorical_cols:
        df[categorical_cols] = df[categorical_cols].fillna('Unknown')

    label_encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    if numeric_cols:
        scaler = MinMaxScaler()
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    df.to_csv('../../data/ebay_smartphones_data.csv', index=False)
