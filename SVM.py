# Felix Hu

# Using Scikit as primary ML library

import numpy as np
import pandas as pd
from sklearn import metrics 
from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_classification
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.utils.class_weight import compute_sample_weight
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pickle # model persistence

# STEP 0 Data

data = pd.read_csv('sqlite_data_ML_iterativeBuild.csv')

# Features we don't care about
del data["id"]
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

train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size = 0.1, random_state = 1337)

# normalization
scale = preprocessing.StandardScaler().fit(train_data)
train_data = scale.transform(train_data)
test_data = scale.transform(test_data)

class_weight = "balanced"

print('Training Features Shape:', train_data.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_data.shape)
print('Testing Labels Shape:', test_labels.shape)
print('Sample weights: '+ str(compute_sample_weight(class_weight=class_weight, y=train_labels)))

# STEP 1 Training

machine = svm.SVC(kernel='rbf')
#machine.fit(train_data, train_labels)
machine.fit(train_data, train_labels, sample_weight=compute_sample_weight(class_weight=class_weight, y=train_labels))
#ada.fit(train_data, train_labels)
# STEP 2 Errors
print("TRAINING ACCURACY: "+str(machine.score(train_data, train_labels)))
print("TESTING ACCURACY: "+str(machine.score(test_data, test_labels)))

predictions = machine.predict(test_data)
conf_mat = confusion_matrix(test_labels, predictions)
print(conf_mat)

#print(rf.feature_importances_)

# STEP 3 Save Ensemble
#filename = 'LogReg_1.sav'
#pickle.dump(ada, open(filename, 'wb'))