#ANOVA 單因子變異數分析
#ANOVA前提：k組母群體均為常態分佈，具有共同變異數，且從k組母群體抽出的樣本彼此間互相獨立 
import numpy as np
import pandas as pd
from scipy import stats

#比較兩種降血壓藥物與控制組對於血壓的改善是否有差異？ H0:治療方式之間並無差異性 H1:治療方式有差異性
control = np.array([147, 158, 148, 146, 145, 151, 147, 153, 163, 144])
drug1 = np.array([151, 137, 141, 152, 147, 133, 143, 148, 132, 146])
drug2 = np.array([146, 152, 154, 155, 137, 152, 149, 145, 138, 152])
combined=np.array([control,drug1,drug2])

#n(總樣本數) & k(組數)
n=len(control)+len(drug1)+len(drug2)
k=len(combined)

# ANOVA檢定統計量：f_oneway() 
(statistic, pvalue)=stats.f_oneway(control, drug1, drug2)
print("statistic is:",statistic)
print("pvalue is:",pvalue)

#計算95%信心水準下f分佈的critical value
#此例中F(df of between=k,df of within=N-k)=F(2, 27) 
alpha=0.05
fdistribution = stats.f(k-1,n-k)
f_critical1 = fdistribution.ppf(0.025)
f_critical2 = fdistribution.ppf(0.975)
print(f_critical1,f_critical2)

#>>statistic is: 3.1533973919011666
#>>pvalue is: 0.058778359393871195
#>>0.025341563254390048 4.242094126533731
#到目前可知檢定統計量3.153<4,242-->代表檢定值落在接受域-->接收虛無假說H0


#進階：計算SSW,SSB,MSW,MSB 來完成ANOVA table
ssw=0
for i in combined:
    ssw+=(i.std(ddof=1)**2)*(len(i)-1)
    print(ssw)
msw=ssw/(n-k)
print("msw:",msw)   

ssb=0
for i in combined:
    ssb+=((i.mean()-combined.mean())**2)*len(i)
    print(ssb)
msb=ssb/(k-1)
print("msb:",msb)

#計算f
f=msb/msw

#建立ANOVA table
df=pd.Series([k-1,n-k,n-1],index=['組間','組內','總計'])
sum_of_squares=pd.Series([ssb,ssw,ssb+ssw],index=['組間','組內','總計'])
mean_squares=pd.Series([msb,msw,' '],index=['組間','組內','總計'])
f_value=pd.Series([f,' ',' '],index=['組間','組內','總計'])
table=pd.DataFrame({'df':df,'SS':sum_of_squares,'MS':mean_squares,'F':f_value})
print(table)
