# import modules
import pandas as pd
import numpy as np

#define the datasets
workbook_1 = 'Data_1.csv'
workbook_2 = 'Data_2.csv'
output_workbook = 'output_data.csv'

#pull in the datasets
df_1 = pd.read_csv(workbook_1)
df_2 = pd.read_csv(workbook_2)

#print(df_1.head(5))
#print(df_2.head(5))

#pull in the data wanted into the new dataset
df_output = pd.merge(df_1, df_1[['ID','PAYER']], on='ID', how ='left')
print(df_output)

df_output.to_csv(output_workbook, index=False)
