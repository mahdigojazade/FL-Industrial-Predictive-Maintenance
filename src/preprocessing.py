import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_data(path):

    data = pd.read_csv(path, sep=" ", header=None)

    data = data.dropna(axis=1)

    cols = ['unit_id', 'cycle'] + \
           [f'op_setting_{i}' for i in range(1,4)] + \
           [f'sensor_{i}' for i in range(1,22)]

    data.columns = cols

    return data


def add_rul(data):

    max_cycle = data.groupby('unit_id')['cycle'].max().reset_index()

    max_cycle.columns = ['unit_id', 'max_cycle']

    data = data.merge(max_cycle, on='unit_id')

    data['RUL'] = data['max_cycle'] - data['cycle']

    return data


def create_label(data):

    data['label'] = (data['RUL'] < 30).astype(int)

    return data


def split_clients(data):

    client_1 = data[data['unit_id'] <= 30]

    client_2 = data[(data['unit_id'] > 30) & (data['unit_id'] <= 70)]

    client_3 = data[data['unit_id'] > 70]

    return client_1, client_2, client_3


def scale_features(client_data):

    features = [col for col in client_data.columns if 'sensor' in col]

    X = client_data[features]

    y = client_data['label']

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled, y
