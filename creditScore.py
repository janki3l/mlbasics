import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import math
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split

#zaczytaj dane z pliku csv
df_train = pd.read_csv("/files/test.csv" , sep = "," , encoding
= 'utf-8')
#sprawdź liczbę kolumn i wierszy
df.shape
df.info()
#wyświetl część tabeli
df_train.head()
#usuń wiersze z duplikatami id
df.drop_duplicates(subset="ID", inplace=True)
