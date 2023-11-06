import pickle

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score

output_file = 'final_model.bin'

# Data cleaning and preparation
df = pd.read_csv('cirrhosis.csv')
df.columns = df.columns.str.lower()
df.dropna(subset=['drug'],inplace=True)
#df = df.fillna(df.mean())

nancolumns=df.columns[df.isna().any()].tolist()
for i in nancolumns:
    df[i]=df[i].fillna(df[i].mean())

status_mapping = {
    'C': 1,
    'CL': 1,
    'D': 0
}

df['status'] = df['status'].replace(status_mapping)

df["age"] = (np.floor(df["age"] / 365.25))

del df['id']
del df['n_days']


df_train, df_val = train_test_split(df, test_size=0.20, random_state=1, stratify=df.status)

y_train = df_train.status.values
y_val = df_val.status.values

del df_train['status']
del df_val['status']

# Training

def train(df_train, y_train, random_state=1):
    train_dicts = df_train.to_dict(orient='records')
    
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(train_dicts)
    
    model = DecisionTreeClassifier(max_depth=20, min_samples_leaf=5, random_state=1)
    model.fit(X_train, y_train)

    return dv, model

def predict(df, dv, model):
    val_dicts = df_val.to_dict(orient='records')

    X_val = dv.transform(val_dicts)
    y_pred = model.predict(X_val)

    return y_pred

# Training the final model
print('training the final model')

dv, model = train(df_train, y_train, random_state=1)
y_pred = predict(df_val, dv, model)

y_test = y_val
acc = accuracy_score(y_test, y_pred)
roc = roc_auc_score(y_val, y_pred)

print('Accuracy: %.3f' % acc)
print('ROC_AUC: %.3f' % roc)


# Save the model

with open(output_file, 'wb') as f_out:
    pickle.dump((dv,model), f_out)

print('Model saved to %s' % output_file)