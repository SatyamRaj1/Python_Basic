from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split  #to import function of test train split 
''' iris=datasets.load_iris()
#spliting in rows and columns
x=iris.data   #features
y=iris.target    #labels
''''''print(x,y)''''''
print(x.shape)   #for rows*columns  print no. of rows and columns  of x  (shape of x array
print(y.shape)    #for rows*colums of y

#trains and testing
#for example analysing study of hours v/s good/bad grades
#with 10 different students
#train with 8 students(observe)
#test/predict 2 students
#to check level accuracy of our model
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
#0.2 test size means 20% of data will be used for testing
print(x_train.shape)   #x(data from above) means features
print(x_test.shape)    #test which is 20% (20% of 150 (above)=120)
print(y_train.shape)   #y means labels
print(y_test.shape)
'''
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn import neighbors, metrics
data=pd.read_csv('car.data')
print(data.head())
x=data[[
    'buying',
    'maint',
    'safety'
    ]].values  #.valuues for case of converting
y=data[['class']]
print(x,y)  
#converting the data
#x by labelencoder
le=LabelEncoder()
for i in range(len(x[0])):   #no.of columns
    x[:,i]=le.fit_transform(x[:,i])  #x[:,i] means all rows and ith column , converting data 
print(x)
#converting y by mapping
label_mapping={
    'unacc':0,
    'acc':1,
    'good':2,
    'vgood':3
    }
y['class']=y['class'].map(label_mapping)
y=np.array(y)
print(y)
knn=neighbors.KNeighborsClassifier(n_neighbors=25,weights-'uniform')  #k=25 
