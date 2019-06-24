from sklearn import datasets      #importing datasets from sklearn

iris=datasets.load_iris()           #loading the iris dataset from datasets into iris object

#print(iris.feature_names)
#print(iris.target_names)

data=iris.data              #loading the data of the iris dataset into data 
target=iris.target          #loading the targets of the iris dataset into target

#print(data.shape)
#print(target.shape)

from sklearn.model_selection import train_test_split

train_data,test_data,train_target,test_target=train_test_split(data,target,test_size=0.5)

from sklearn.neighbors import KNeighborsClassifier

clsfr=KNeighborsClassifier(n_neighbors=3)    #KNN algorithm is loaded to clsfr

clsfr.fit(train_data,train_target)  #training the algorithm

results=clsfr.predict(test_data)

print('Actual Results:',test_target)
print('Presdicted Results:',results)

from sklearn.metrics import accuracy_score

accuracy=accuracy_score(test_target,results)

print('Accuracy:',accuracy)

