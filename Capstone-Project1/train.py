import xgboost as xgb
import numpy as np
import pandas as pd

import pickle

from sklearn.preprocessing import LabelEncoder

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer

from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score

output_file = 'final_model.bin'

df = pd.read_csv('data/ObesityDataSet.csv')

df.columns = df.columns.str.lower()
df = df.rename(columns={'nobeyesdad': 'obesity_level'})

#Encoding categorical variables
le = LabelEncoder()
df = df.apply(le.fit_transform)



df_train, df_val = train_test_split(df, test_size=0.20, random_state=1, stratify=df.obesity_level)


xgb_params = {
    'eta': 0.3,
    'max_depth': 5,
    'min_child_weight':10,

    'objective': 'multi:softmax',
    'num_class': 7,
    'eval_metric': 'logloss',

    'nthread': 8,
    'seed': 1,
    'verbosity': 1
}

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)

y_train = df_train.obesity_level.values
y_val = df_val.obesity_level.values

del df_train['obesity_level']
del df_val['obesity_level']



# Training
def train(df_train, y_train):
    dicts = df_train.to_dict(orient='records')
    
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)
    
    features = dv.feature_names_
    dtrain = xgb.DMatrix(X_train, label= y_train, feature_names=features)

    model = xgb.train(xgb_params, dtrain, num_boost_round = 300 )
    
    return dv, model

def predict(df, y_val, dv, model):
    dicts = df.to_dict(orient='records')

    X_val = dv.transform(dicts)
    features = dv.feature_names_ 
    dval = xgb.DMatrix(X_val, label=y_val, feature_names=features)
    
    y_pred = model.predict(dval)
    probabilities = model.predict(dval, output_margin=True)
    probabilities = np.exp(probabilities) / np.sum(np.exp(probabilities), axis=1, keepdims=True)

    return y_pred, probabilities


# Training the final model
print('training the final model')

dv, model = train(df_train, y_train)
y_pred, probabilities = predict(df_val,y_val, dv, model)


auc = roc_auc_score(y_val, probabilities , multi_class='ovr')

print('AUC: %.3f' % auc)

#Saving the model
with open(output_file, 'wb') as f_out:
    pickle.dump((dv,model), f_out)

print('Model saved to %s' % output_file)








