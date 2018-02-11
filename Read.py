import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#pandas xlsx read
data = pd.read_excel('Test.xlsx')
#pandas csv read
data_csv = pd.read_csv('Test.csv')

#python csv read
import csv
f = open('Test.csv', 'r')
rdr = csv.reader (f)
i = 0
matrix = []
for line in rdr:
    matrix.append(line)
    print(line)
    i = i+1
f.close