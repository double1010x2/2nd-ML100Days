import numpy as np
import pandas as pd

app_train = pd.read_csv("./application_train.csv")

# row and columns
row, column = app_train.shape

print ("row=%d, columns=%d" %(row, column))
# print all keys
app_train_keys = app_train.columns
print (app_train_keys)

# slice by some columns
SK_ID_CURR_AND_TARGET = app_train[["SK_ID_CURR", "TARGET"]]
print (SK_ID_CURR_AND_TARGET)
# slice by some rows
ff = np.random.randint(low=0, high=row-1, size = 100)
app_train_100 = app_train.iloc[ff]
print (app_train_100)
