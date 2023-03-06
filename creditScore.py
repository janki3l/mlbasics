import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import math
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split


df_train = pd.read_csv("./files/train.csv" , sep = "," , encoding = 'utf-8')

#print(df_train.shape)
#print(df_train.info())

#usuń wiersze z duplikatami id

df_train.drop_duplicates(subset="ID", inplace=True)


print(df_train.describe())