import os
import numpy as np
import sys
from DBconn import DBConnection
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
from tensorflow.keras.utils import img_to_array,load_img
from keras.models import load_model
import pickle
def calculate_svm_accuracy(x_test,y_test):
     try:
         database = DBConnection.getConnection()
         cursor = database.cursor()
         print("CALCULATING SVM ACCURACY......")
         model = open('..\\PlantDiseaseDetection\\SVM.model', 'rb')
         clf_svm = pickle.load(model)
         predicted = clf_svm.predict(x_test)
         accuracy_svm = accuracy_score(y_test, predicted) * 100
         '''pre_svm = precision_score(y_test, predicted, average="macro") * 100
         recall_svm = recall_score(y_test, predicted, average="macro") * 100
         fscore_svm = f1_score(y_test, predicted, average="macro") * 100
         print(accuracy_svm,pre_svm,recall_svm,fscore_svm)'''

         
         sql = "update evaluations set svm='"+str(accuracy_svm)+"' where sno=1"
         cursor.execute(sql)
         database.commit()


     except Exception as e:
        #print("Error=" +e.args[0])
         tb = sys.exc_info()[2]
         print(tb.tb_lineno)