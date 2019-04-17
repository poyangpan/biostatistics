#獨立性檢定
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import chisquare

#分析有無吸菸跟是否得到肺癌有關係？ H0:抽煙與肺癌有關 H1:抽煙與肺癌無關
#用pandas series建立DataFrame
smoke=pd.Series({'cancer':28,'no_cancer':39}) #有抽煙，得肺癌跟沒得肺癌人數
no_smoke=pd.Series({'cancer':24,'no_cancer':79}) #沒抽煙，得肺癌跟沒得肺癌人數
observed=pd.DataFrame({'smoke':smoke,'no_smoke':no_smoke}) #組合兩筆資料呈DataFrame
print('observed')
print(observed)

#欄總和
col_totals=observed.sum()

#列總和 axis設定為1去計算列的加總
row_totals=observed.sum(axis=1)

#總和
total=observed.sum().sum()

#計算期望值
#把行總計X列總計/總計=期望值，在此把row_totals與col_totals取外積-->得到2x2的二維陣列
expected=np.outer(row_totals[0:2],col_totals[0:2])/total
#把二維陣列轉換成DataFrame
expected=pd.DataFrame(expected)
#幫DataFrame加上index&columns名稱
expected.columns=["smoke","no_smoke"]
expected.index=["cancer","no_cancer"]
print('expected')
print(expected)

#計算chi-square
chi_squared_stat = (((observed-expected)**2)/expected).sum().sum()
print("chi_squared_stat=",chi_squared_stat)
#計算critical value
crit = stats.chi2.ppf(q = 0.95,df = 1) 
print("Critical value=",crit)
#計算p value
pvalue = 1 - stats.chi2.cdf(x=chi_squared_stat, df=1)
print("P value=",pvalue)

#>>chi_squared_stat= 6.5366147830737855
#>>Critical value= 3.841458820694124
#>>P value= 0.010567625307906559
#檢定統計量=6.536>3.841 -->拒絕虛無假說-->代表抽菸跟肺癌無關

