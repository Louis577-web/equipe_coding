from ucimlrepo import fetch_ucirepo 
import pandas as pd

# fetch dataset 
bone_marrow_transplant_children = fetch_ucirepo(id=565) 
  
# data (as pandas dataframes) 
x = bone_marrow_transplant_children.data.features 
y = bone_marrow_transplant_children.data.targets 

# metadata 
print(bone_marrow_transplant_children.metadata) 
  
# variable information 
print(bone_marrow_transplant_children.variables) 




df=pd.DataFrame(x)
print("columns" ,df.columns)
print("shape",df.shape)

x = df.copy()
y = pd.Series(y)


print(df.head)
A=df.copy()
print(A)
colonnes_manquantes=A.columns[A.isnull().sum()>0]

for col in colonnes_manquantes:
    if A[col].dtype in ["int64","float64"]:
        A[col].fillna(A[col].median(),inplace=True)

    elif A[col].nunique() == 2:
        A[col].fillna(A[col].mode()[0],inplace=True)
    elif A[col].dtype=="object":
        A[col].fillna("inconnue",inplace=True)


df=A



print(f"x:{x.shape} y:{y.shape}")

import sqlite3






