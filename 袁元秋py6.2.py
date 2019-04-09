
import pandas as pd
a = [1,2,3,4,5]
b=['mayi','jack','tom','rain','hanmeimei']
c=[18,21,25,19,23]
d=[99,89,95,80,81]


dataframe = pd.DataFrame({'No.':a,'Name':b,'Age':c,'Score':d})

dataframe.to_csv("test.csv",index=False,sep=',')
