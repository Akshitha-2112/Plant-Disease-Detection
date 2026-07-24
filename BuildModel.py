import os

from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
import pickle
from sklearn.svm import SVC
import sys
from sklearn.model_selection import train_test_split


def build_model(x_train,y_train):
    try:
        x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.3, random_state=42)

        #KNN
        print("[INFO] Training KNN model...")
        clf_knn = KNeighborsClassifier()
        clf_knn.fit(x_train, y_train)
        with open('KNN.model', 'wb') as f:
            pickle.dump(clf_knn, f)
        print("[INFO] Training KNN model created successfully..!")

        #SVM
        print("[INFO] Training SVM model...")
        clf_svm =SVC(kernel='linear',decision_function_shape='ovr')
        clf_svm.fit(x_train, y_train)
        with open('SVM.model', 'wb') as f:
            pickle.dump(clf_svm, f)
        print("[INFO]  Training SVM model created successfully..!")

        return x_test,y_test


    except Exception as e:
        print("Error=" + e.args[0])
        tb = sys.exc_info()[2]
        print(tb.tb_lineno)



