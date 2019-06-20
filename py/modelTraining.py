


import pandas as pd
import lightgbm as lgb
import numpy as np
import seaborn as sns
import json

# For the sake of simplicity, only including the following variables in the model
trainFeat = [
      'LotArea'
    , 'Neighborhood'
    , 'Condition1'
    , 'Condition2'
    , 'OverallQual'
    , 'OverallCond'
    , 'YearBuilt'
    , 'SaleCondition'
]

trainRaw = pd.read_csv("Storage/tabularData/train.csv", usecols=['Id'] + trainFeat + ['SalePrice'])

# Need to know they're categories.
for feat in trainRaw.columns[trainRaw.dtypes == 'object']:
    trainRaw[feat]=trainRaw[feat].astype('category')

lgbMat = lgb.Dataset(data = trainRaw.loc[:,trainFeat], label=trainRaw.SalePrice)

lgbPars = {
      'objective':'regression'
    , 'learning_rate':0.05
    , 'metric':'rmse'
    , 'lambda_l1':0
    , 'verbose':-1
    , 'num_leaves':5
    , 'feature_fraction':0.75
    , 'bagging_fraction':0.75
    , 'max_depth':3
    , 'lambda_l2':2
    , 'min_child_weight':100
}

# How many trees should we grow?
lgbCV = lgb.cv(params=lgbPars, train_set=lgbMat, num_boost_round=10000, nfold=10, stratified=True, early_stopping_rounds=10)

# Train the model
lgbModel = lgb.train(lgbPars,lgbMat, num_boost_round=np.argmin(lgbCV['rmse-mean']))

# Save the model and training data. The web service will load this and return predictions from the POST payload.
lgbModel.save_model(filename="Storage/models/lgbModel")
trainRaw.to_pickle("Storage/tabularData/modelTraining")

# Check the distribution of predictions to make sure nothing skunky happened.
sns.distplot(lgbModel.predict(trainRaw.loc[:,trainFeat]))