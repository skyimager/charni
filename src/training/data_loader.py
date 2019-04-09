import os
import pandas as pd
import numpy as np

def build_source(base_path):
    
    train_txt = os.path.join(base_path,"train.txt")
    val_txt = os.path.join(base_path,"validation.txt")
    test_txt = os.path.join(base_path,"test.txt")
    
    data_train = pd.read_csv(train_txt, sep=" ", names=["file_path", "label"])
    data_val = pd.read_csv(val_txt, sep=" ", names=["file_path", "label"])
    data_test = pd.read_csv(test_txt, sep=" ", names=["file_path", "label"])
    
    print("\nPrinting unique labels")
    X_train = data_train["file_path"].values
    y_train = data_train["label"].values
    print("for train:", np.unique(y_train))
    
    X_val = data_val["file_path"].values
    y_val = data_val["label"].values
    print("for val:", np.unique(y_val))
    
    X_test = data_test["file_path"].values
    y_test = data_test["label"].values
    print("for test:", np.unique(y_test))
    
    return X_train, y_train, X_val, y_val, X_test, y_test