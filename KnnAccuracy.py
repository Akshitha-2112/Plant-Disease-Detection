import os
import numpy as np
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
from DBconn import DBConnection

import pickle

def calculate_Accuracy_knn(x_test,y_test):

    try:
        print("CALCULATING KNN ACCURACY......")
        database = DBConnection.getConnection()
        cursor = database.cursor()
        model = open('..\PlantDiseaseDetection\KNN.model', 'rb')
        clf_knn = pickle.load(model)
        predicted = clf_knn.predict(x_test)
        accuracy_knn = accuracy_score(y_test, predicted) * 100
        '''pre_knn = precision_score(y_test, predicted, average="macro") * 100
        recall_knn = recall_score(y_test, predicted, average="macro") * 100
        fscore_knn = f1_score(y_test, predicted, average="macro") * 100
        print(accuracy_knn,pre_knn,recall_knn,fscore_knn)'''

        sql = "update evaluations set knn='"+str(accuracy_knn)+"' where sno=1"
        cursor.execute(sql)
        database.commit()



    except Exception as e:
        print("Error=" ,e.args[0])
    #     tb = sys.exc_info()[2]
    #     print(tb.tb_lineno)



