import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_validate
import warnings


def predict(test_size, metrics):
  df = pd.read_csv("datasetMaior6.csv", sep=";")
  df.head()

  df.shape

  X = df.iloc[:,0:20].values
  y = df.iloc[:, 20].values

  labelencoder_Y = LabelEncoder()
  y = labelencoder_Y.fit_transform(y)

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size, stratify = y,shuffle = True, random_state = 1)
  print(len(X_train),len(X_test),len(y_train),len(y_test))

  warnings.filterwarnings("ignore")

  chosen_metrics = metrics.split("\n")
  print(chosen_metrics)
  
  scoring = {'acc': 'accuracy', 
              'precision_macro': 'precision_macro',
              'recall_macro': 'recall_macro', 
              'f1_macro': 'f1_macro', 
              'precision_micro': 'precision_micro',
              'recall_micro': 'recall_micro', 
              'f1_micro': 'f1_micro'}
  models = []
  precision_LR = []
  precision_LDA = []
  precision_KNN = []
  precision_CART= []
  precision_NB = []
  precision_SVM = []

  recall_LR = []
  recall_LDA = []
  recall_KNN = []
  recall_CART = []
  recall_NB = []
  recall_SVM = []

  f1_LR = []
  f1_LDA = []
  f1_KNN = []
  f1_CART = []
  f1_NB = []
  f1_SVM = []


  models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
  models.append(('LDA', LinearDiscriminantAnalysis()))
  models.append(('KNN', KNeighborsClassifier()))
  models.append(('CART', DecisionTreeClassifier()))
  models.append(('NB', GaussianNB()))
  models.append(('SVM', SVC(gamma='auto')))
    # evaluate each model in turn
  results = []
  names = []
  for name, model in models:
    print(name)
    kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True) 

    cv_results = cross_validate(estimator=model, X=X_train, y=y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)

    print("Acurácia: %f" % (cv_results['test_acc'].mean()))

    if name == 'LR':
      precision_LR = cv_results['test_precision_macro']
      recall_LR = cv_results['test_recall_macro']
      f1_LR = cv_results['test_f1_macro']

    elif name == 'LDA':
      precision_LDA = cv_results['test_precision_macro']
      recall_LDA = cv_results['test_recall_macro']
      f1_LDA = cv_results['test_f1_macro']

    elif name == 'KNN':
      precision_KNN = cv_results['test_precision_macro']
      recall_KNN = cv_results['test_recall_macro']
      f1_KNN = cv_results['test_f1_macro']

    elif name == 'CART':
      precision_CART= cv_results['test_precision_macro']
      recall_CART = cv_results['test_recall_macro']
      f1_CART = cv_results['test_f1_macro']


    elif name == 'NB':
      precision_NB = cv_results['test_precision_macro']
      recall_NB = cv_results['test_recall_macro']
      f1_NB = cv_results['test_f1_macro']


    elif name == 'SVM':
      precision_SVM = cv_results['test_precision_macro']
      recall_SVM = cv_results['test_recall_macro']
      f1_SVM = cv_results['test_f1_macro']


      #Macro
    print("Precisão macro: %f" % (cv_results['test_precision_macro'].mean()))
    print("Recall macro: %f" % (cv_results['test_recall_macro'].mean()))
    print("f1 Score macro: %f" % (cv_results['test_f1_macro'].mean()))

    #Micro
    print("Precisão micro: %f" % (cv_results['test_precision_micro'].mean()))
    print("Recall micro: %f" % (cv_results['test_recall_micro'].mean()))
    print("f1 Score micro: %f" % (cv_results['test_f1_micro'].mean()))

    cv_results.keys()
    data_precision = [precision_LR, precision_LDA, precision_KNN, precision_CART, precision_NB, precision_SVM]
    data_recall = [recall_LR, recall_LDA, recall_KNN, recall_CART, recall_NB, recall_SVM]
    data_f1_score = [f1_LR, f1_LDA, f1_KNN, f1_CART, f1_NB, f1_SVM]

def plot_comparison_graph(self, data_precision, data_recall, data_f1_score):

  fig = plt.figure(figsize =(10, 7))
  ax = fig.add_axes([0, 0, 1, 1])
  bp = ax.boxplot(data_precision)
  ax.set_xticklabels(['LR', 'LDA', 'KNN', 'CART', 'NB', 'SVM'])
  plt.title("Algorithm Comparison - Precision")
  plt.show()

  fig = plt.figure(figsize =(10, 7))
  ax = fig.add_axes([0, 0, 1, 1])
  bp = ax.boxplot(data_recall)
  ax.set_xticklabels(['LR', 'LDA', 'KNN', 'CART', 'NB', 'SVM'])
  plt.title("Algorithm Comparison - Recall")
  plt.show()

  fig = plt.figure(figsize =(10, 7))
  ax = fig.add_axes([0, 0, 1, 1])
  bp = ax.boxplot(data_f1_score)
  ax.set_xticklabels(['LR', 'LDA', 'KNN', 'CART', 'NB', 'SVM'])
  plt.title("Algorithm Comparison - F1 score")
  plt.show()