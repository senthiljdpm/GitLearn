# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 22:22:38 2018
@author: senth
Spark SQL Test
"""

import pandas as pd
import numpy as np
#%%
if __name__ == '__main__':
    dct = { 'EmpId': [1,2,3,4,5,6,7,8,9,10],
            'DeptNo': [10, 20, 30, 10, 40, 10, 30, 20, 50, 40],
            'Sal': [343,1234,112,1323,12424,123,113,112,465,55]
          }

    df = pd.DataFrame(dct)
    
    # Count over partition by 
    df['CntOver'] = df.groupby('DeptNo')['DeptNo'].transform(len)
    
    # RowNum over partition by 
    df = df.assign(
                    RowNum = df.sort_values('Sal', ascending=False)
                               .groupby('DeptNo')
                               .cumcount()+1
                  )
    
    # Min, Max and Mean sal for every dept
    dfAggrSal = df.groupby('DeptNo').agg({'Sal': 
                                            {'Mean': np.mean, 
                                             'Min': np.min, 
                                             'Max': np.max}}
                                        ).reset_index()
        
    # Sum of Sal group by DeptNo
    dfAggrSum = df.groupby('DeptNo')['Sal'].sum().reset_index()