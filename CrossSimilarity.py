# measure agreement between two SKLearn models
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
import pickle
import numpy as np
import pandas as pd

f1 = "GradBoost_1_P70L30.sav"
f2 = "Adaboost_1_P70L30.sav"

m1 = pickle.load(open(f1, 'rb'))
m2 = pickle.load(open(f2, 'rb'))

data = pd.read_csv('sqlite_data_ML_iterativeBuild_P70L30.csv')

# remove unnecessary features
del data["id"]
del data["option_expiration"]
del data["flow_ticker"]
del data["flow_order_time"]
del data["order_status"]
del data["symbol"]
del data["events"]
del data["sector"]

data = data.dropna(how='any')

data = pd.get_dummies(data, columns=["option_call_or_put", "option_order_type"])

print("Number of unprofitable vs profitable:")
print(data["profitable"].value_counts())

labels = np.array(data["profitable"])
data = data.drop("profitable", axis = 1)
print(data.columns)

data = np.array(data)

predicted1 = m1.predict(data)
predicted2 = m2.predict(data)

match = 0
true_pos = 0
false_pos = 0
for index in range(len(data)):
    if predicted1[index] == predicted2[index]:
        match+=1
    if predicted1[index] == predicted2[index] and predicted1[index] == 1 and labels[index] == 1:
        true_pos+=1
    if predicted1[index] == predicted2[index] and predicted1[index] == 1 and labels[index] == 0:
        false_pos+=1

# means nothing, basically training error
print("Matches: "+str(match))
print("Total: "+str(len(data)))
print("True Pos: "+str(true_pos))
print("False Pos: "+str(false_pos))
print("Total Pos: "+str(np.count_nonzero(labels==1)))


