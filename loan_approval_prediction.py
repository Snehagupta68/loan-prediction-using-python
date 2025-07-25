import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import svm

df=pd.read_excel("Loan.xlsx")
df.head()
df.info()
print("missing values:\n")
df.isnull().sum()

df["loanAmount_log"]=np.log(df['LoanAmount'])
df["loanAmount_log"].hist(bins=20)

df.isnull().sum() 
df["totalIncome"]=df["ApplicantIncome"]+df["CoapplicantIncome"]
df["totalIncome_log"]=np.log(df["totalIncome"])
df["totalIncome"].hist(bins=20)

df["Gender"].fillna(df["Gender"].mode()[0], inplace=True)
df["Married"].fillna(df["Married"].mode()[0], inplace=True)
df["Self_Employed"].fillna(df["Self_Employed"].mode()[0], inplace=True)
df["Dependents"].fillna(df["Dependents"].mode()[0], inplace=True)

df.LoanAmount = df.LoanAmount.fillna(df.LoanAmount.mean())
df.loanAmount_log = df.loanAmount_log.fillna(df.loanAmount_log.mean())

df["Loan_Amount_Term"].fillna(df["Loan_Amount_Term"].mode()[0], inplace=True)
df["Credit_History"].fillna(df["Credit_History"].mode()[0], inplace=True)

df.isnull().sum()

x= df.iloc[:, np.r_[1:5,9:11,13:15]].values
y= df.iloc[:,12].values

x
y

print("per of missing gender is %2f%% " % ((df["Gender"].isnull().sum()/df.shape[0])*100)) 
print("number of people who take loans as per group by gender")
print(df["Gender"].value_counts())

sns.countplot(x="Gender", data=df, palette="Set1")

print("number of people who take loans as per group by martial status")
print(df["Married"].value_counts())

sns.countplot(x="Married", data=df, palette="Set2")

print("number of people who take loans as per group by education")
print(df["Education"].value_counts())

sns.countplot(x="Education", data=df, palette="Set1")

print("number of people who take loans as per group by Dependents")
print(df["Dependents"].value_counts())

sns.countplot(x="Dependents", data=df, palette="Set1")

print("number of people who take loans as per group by Employment")
print(df["Self_Employed"].value_counts())

sns.countplot(x="Self_Employed", data=df, palette="Set1")

print("number of people who take loans as per group by Loan Amount")
print(df["LoanAmount"].value_counts())

sns.countplot(x="LoanAmount", data=df, palette="Set1")

print("number of people who take loans as per group by Credit history")
print(df["Credit_History"].value_counts())

sns.countplot(x="Credit_History", data=df, palette="Set1")
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x,y, test_size= 0.2, random_state=0)

from sklearn.preprocessing import LabelEncoder
Labelencoder_x = LabelEncoder()


for i in range(0,5):
    X_train[:,i]= Labelencoder_x.fit_transform(X_train[:,i].astype(str))
    X_train[:,7]= Labelencoder_x.fit_transform(X_train[:,7].astype(str))

X_train

Labelencoder_y=LabelEncoder()
y_train= Labelencoder_y.fit_transform(y_train)

y_train

for i in range(0,5):
    X_test[:,i]= Labelencoder_x.fit_transform(X_test[:,i])
    X_test[:,7]= Labelencoder_x.fit_transform(X_test[:,7])

X_test

Labelencoder_y=LabelEncoder()
y_test= Labelencoder_y.fit_transform(y_test)

y_test

from sklearn.preprocessing import StandardScaler

ss= StandardScaler()
X_train= ss.fit_transform(X_train)
X_test= ss.fit_transform(X_test)

from sklearn.ensemble import RandomForestClassifier

rf_clf =RandomForestClassifier()
rf_clf.fit(X_train,y_train)

from sklearn import metrics
y_pred = rf_clf.predict(X_test)

print("accuracy of random forest clf is:", metrics.accuracy_score(y_pred,y_test))
y_pred

from sklearn.neighbors import KNeighborsClassifier
KNN =KNeighborsClassifier(n_neighbors=3)
KNN.fit(X_train,y_train)

from sklearn import metrics
y_pred = KNN.predict(X_test)

print("accuracy of 3 nearest neighbor clf is:", metrics.accuracy_score(y_pred,y_test))
y_pred

from sklearn.naive_bayes import GaussianNB
nb_clf=GaussianNB()
nb_clf.fit(X_train,y_train)

from sklearn import metrics
y_pred = nb_clf.predict(X_test)

print("accuracy of naive bayes clf is:", metrics.accuracy_score(y_pred,y_test))
y_pred
from sklearn.tree import DecisionTreeClassifier
dt_clf=DecisionTreeClassifier()
dt_clf.fit(X_train,y_train)

from sklearn import metrics
y_pred = dt_clf.predict(X_test)

print("accuracy of decision tree clf is:", metrics.accuracy_score(y_pred,y_test))
y_pred

print("Hence , naive bayes classifier is the best approach to use for prediction")










































