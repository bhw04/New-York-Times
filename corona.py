# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 21:08:00 2021

@author: ABO NAZIH
"""

import pandas as pd
import matplotlib.pyplot as plt

corona= {"2019": [20, 8, 22, 17, 40.17],"2020": [73, 44, 76.44, 51.3, 88], "2021": [18, 10.6, 21.7, 13.8, 23]}

print(corona)

print()

coronadf= pd.DataFrame(corona, columns=["2019", "2020", "2021"])
coronadf.index=index=["China", "Spain", "USA", "United Kingdom", "Italy"]
#print(coronadf)

coronadf.name= "Infections/Years"
coronadf.index.name="Countries"
coronadf.columns.name="Years"
print(coronadf)

coronadf.plot(kind="bar", style="r-x", legend="True", title="Percentage of infected countries in the past three years", rot=45 )

