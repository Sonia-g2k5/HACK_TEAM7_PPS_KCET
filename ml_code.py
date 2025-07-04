# -*- coding: utf-8 -*-
"""ml_code.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1higXUhpXGBWMF9bFHRd4w90iEaMtNwRW

**IMPORTING THE NEEDED LIBRARIES**
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression

"""**LOADING THE DATA**"""

dia=pd.read_csv('/content/dataset.csv')

"""**VIEWING THE DATA**"""

dia.head()

"""CLEANING THE DATA
CHECKING FOR NULL VALUES **bold text**
"""

dia.isnull().sum()



dia.columns

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
dia['Genre_no']=le.fit_transform(dia['Genre preference'])
dia['Like_no']=le.fit_transform(dia['You like leo movie or you don\'t like'])
dia['Actor or director familiarity_no']=le.fit_transform(dia['Actor or director familiarity'])
dia['previous liking for similar movies_no']=le.fit_transform(dia['previous liking for similar movies'])
dia["Duration of the trailer watched_no"]=le.fit_transform(dia["Duration of the trailer watched "])

"""**SPLITING THE DEPENDENT AND INDEPENDENT VARIABLES**"""

indep=dia[['Genre_no', 'Interest after watching trailer(1-5)',
       'Actor or director familiarity_no', 'Duration of the trailer watched_no',
       'previous liking for similar movies_no']]
dep=dia[["Like_no"]]


X_train, X_test, y_train, y_test = train_test_split(indep, dep, test_size=0.2, random_state=42)

# Create and train the Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
accuracy = accuracy_score(y_test, y_pred)
print("Model Evaluation Metrics:")
print(f"Accuracy : {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall   : {recall:.2f}")
print(f"F1 Score : {f1:.2f}")

dia.head()

G=int(input("Enter the Genre preference:\nAction/Thriller - 0\nHorror - 3\nComedy - 1\nFantacy - 2"))
inter=int(input("Enter the Interest after watching trailer(1-5):"))
re=int(input("I loved them - 2\nthey were okay - 4\nI didnt like them - 0\nI havent watched similar movies - 1\nI am not sure - 3"))
act=int(input("Enter the Actor or director familiarity:\nExtremely familiar - 0\nNot at all familiar - 1\nSlightly familiar - 2\nVery familiar - 3"))
like=int(input("Enter 0 if you like leo movie or 1 if you don't like:"))
ans=model.predict([[G,inter,re,act,like]])
if ans==1:
  print("You will like leo movie")
else:
  print("You will not like leo movie")



import pickle

# Save the trained model to a file
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model saved as 'model.pkl'")
