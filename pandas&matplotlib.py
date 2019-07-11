from __future__ import print_function

import pandas as pd
import matplotlib.pyplot as plt

#create series
name=pd.Series(['A','B','C','D','E','F'])
salary=pd.Series([10000,20000,30000,15000,13000,25300])

#create dataFrame
info=pd.DataFrame({'name': name,'salary':salary})
hist=info.hist('salary')

#judge series
salary.apply(lambda val:val>15000)

#alter dataframe
info['salary/1000']=info['salary']/1000

print(info)

pd_salary=info['salary']
plt.axis((0, 5, 0, 35000))
plt.plot(pd_salary)
plt.show()