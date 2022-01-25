#### This code is copied taken from https://www.tutorialspoint.com/fraud-detection-in-python 
#### This is meant strictly for Study Purposes

import pandas as pd
#Load the creditcard.csv using pandas
datainput = pd.read_csv("s3://myawscloud.uk/creditcard.csv")
false = datainput[datainput['Class'] == 1]
true = datainput[datainput['Class'] == 0]
n = len(false)/float(len(true))
print(n)
print('False Detection Cases: {}'.format(len(datainput[datainput['Class'] == 1])))
print('True Detection Cases: {}'.format(len(datainput[datainput['Class'] == 0])),"\n")

print("This code is copied taken from https://www.tutorialspoint.com/fraud-detection-in-python ")
