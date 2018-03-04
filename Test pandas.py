
import pandas as pd
from glob import glob

#xlsx 열기
df = pd.read_excel('DB_Sample.xlsx', sheetname='Sheet1')
print(df)
print(df['Int. Avg.'])

#csv 열기
df = pd.read_csv('1. Albert\data_csv.csv')
print(df)

#File List 출력
FileList = glob('*.py')
print(FileList)