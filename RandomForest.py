# Felix Hu

# Using Scikit as primary ML library

import numpy as np
import pandas as pd
from sklearn import metrics 
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.utils.class_weight import compute_sample_weight
import pickle # model persistence

# STEP 0 Data

data = pd.read_csv('sqlite_data_ML_iterativeBuild.csv')

# Features we don't care about
del data["option_expiration"]
del data["flow_ticker"]
del data["flow_order_time"]
del data["order_status"]
del data["symbol"]
del data["events"]
del data["sector"]

# TEMP, we actually want these but they contain Nans
# print(data.isna().any())

data = data.dropna(how='any')

data = pd.get_dummies(data, columns=["option_call_or_put", "option_order_type"])

print("Number of unprofitable vs profitable:")
print(data["profitable"].value_counts())

labels = np.array(data["profitable"])
data = data.drop("profitable", axis = 1)
print(data.head(5))

feature_list = list(data.columns)
data = np.array(data)

train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size = 0.1, random_state = 42)

print('Training Features Shape:', train_data.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_data.shape)
print('Testing Labels Shape:', test_labels.shape)

# STEP 1 Training

rf = RandomForestClassifier(n_estimators = 200, random_state = 1337, oob_score = True)
rf.fit(train_data, train_labels, sample_weight=compute_sample_weight(class_weight='balanced', y=train_labels))

# STEP 2 Out of Bag Error and other Errors
print("TRAINING ACCURACY: "+str(rf.score(train_data, train_labels)))
print("OOB ACCURACY: "+str(rf.oob_score_))
print("TESTING ACCURACY: "+str(rf.score(test_data, test_labels)))

predictions = rf.predict(test_data)
conf_mat = confusion_matrix(test_labels, predictions)
print(conf_mat)

#print(rf.feature_importances_)

# STEP 3 Save Ensemble
#filename = 'RandomForest_1.sav'
#pickle.dump(rf, open(filename, 'wb'))