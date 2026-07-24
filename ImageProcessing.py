import os
import numpy as np
#from keras.preprocessing import image
from tensorflow.keras.utils import img_to_array,load_img
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import pickle
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import sys
from sklearn.neural_network import MLPClassifier
def features_extraction():
    try:
        print("[INFO] Loading Training dataset images...")
        DIRECTORY = "..\\PlantDiseaseDetection\\dataset"
        CATEGORIES=['Corn_Common_rust','Grape_Leaf_blight','Orange_Haunglongbing','Peach_Bacterial_spot'
                    ,'Peach_healthy','Pepper_bell_Bacterial_spot','Potato_healthy','Soybean_healthy',
                    'Strawberry_Leaf_scorch','Tomato_mosaic_virus']

        data = []
        clas = []

        for category in CATEGORIES:

            path = os.path.join(DIRECTORY, category)

            for img in os.listdir(path)[:150]:
                img_path = os.path.join(path, img)
                img = load_img(img_path, target_size=(128,128))
                img = img_to_array(img)
                img = img / 255
                data.append(img)
                clas.append(category)

        x_train = np.array(data)
        x_train = x_train.reshape(len(x_train), -1)
        y_train = np.array(clas)


        print("[INFO] Image Processing completed")

        return x_train,y_train
    except Exception as e:
        #print("Error=" + e.args[0])
        tb = sys.exc_info()[2]
        print(tb.tb_lineno)

