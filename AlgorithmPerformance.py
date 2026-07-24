import os
import numpy as np
import sys
from Graph import view
from DBconn import DBConnection
from KnnAccuracy import calculate_Accuracy_knn
from Svm_Accuracy import calculate_svm_accuracy
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
def calculate_Accuracy(x_test,y_test):
    try:

        calculate_svm_accuracy(x_test,y_test)
        calculate_Accuracy_knn(x_test,y_test)
        database = DBConnection.getConnection()
        cursor = database.cursor()
        cursor.execute("select svm,knn,cnn,vgg16 from evaluations")
        row=cursor.fetchall()
        for r in row:
            svm=r[0]
            knn=r[1]
            cnn=r[2]
            vgg16=r[3]




        list = []
        list.clear()
        list.append(float(svm))
        list.append(float(knn))
        list.append(float(cnn))
        list.append(float(vgg16))
        view(list)


         
    except Exception as e:
        print("Error=" , e.args[0])
        tb = sys.exc_info()[2]
        print(tb.tb_lineno)
   
    
    
   
   
