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

class LDA:

  def predict(self, test_size, metrics):
    df = pd.read_csv("/home/victoria/Documents/BIOD/projeto-redes-neurais/datasetMaior6.csv", sep=";")
    df.head()

    df.shape

    X = df.iloc[:,0:20].values
    y = df.iloc[:, 20].values

    labelencoder_Y = LabelEncoder()
    y = labelencoder_Y.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size, stratify = y,shuffle = True, random_state = 1)

    warnings.filterwarnings("ignore")

    chosen_metrics = metrics.split("\n")
    scoring = ""
    m = ""
    for metric in chosen_metrics:
      if "Accuracy" in metric:
        print(metric)
        scoring += "accuracy,"
      if "Precision" in metric:
        print(metric)
        scoring+=("precision_macro,")

    model = ('LDA', LinearDiscriminantAnalysis())
    kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True) 

    cv_results = cross_validate(estimator=model, X=X_train, y=y_train, cv=kfold, scoring=scoring)
    results = cv_results

    for metric in chosen_metrics:
      if "Accuracy" in metric:
        print("Acurácia: %f" % (cv_results['test_accuracy'].mean()))

      if "Precision" in metric:
        print("Precisão macro: %f" % (cv_results['test_precision_macro'].mean()))


        #Macro
      # print("Recall macro: %f" % (cv_results['test_recall_macro'].mean()))
      # print("f1 Score macro: %f" % (cv_results['test_f1_macro'].mean()))

      # #Micro
      # print("Precisão micro: %f" % (cv_results['test_precision_micro'].mean()))
      # print("Recall micro: %f" % (cv_results['test_recall_micro'].mean()))
      # print("f1 Score micro: %f" % (cv_results['test_f1_micro'].mean()))

    cv_results.keys()
      