#適合度檢定(goodness of fit test)
import numpy as np
import pandas as pd
import scipy.stats as stats

#將基因型為Aa的作物進行雜交取得後代，理論上會得到三種基因型:AA, Aa, aa，且比例應為1:2:1。
#今天我們獲得的試驗結果，100個後代基因型為AA:18, Aa:55, aa:27。請問我們的結果是否符合上述的遺傳模式？
plant=pd.DataFrame(["AA"]*18+["Aa"]*55+["aa"]*27)
observed= pd.crosstab(index=plant[0], columns="count")
expected_count=pd.DataFrame(["AA"]*25+["Aa"]*50+["aa"]*25)
expected=pd.crosstab(index=expected_count[0], columns="count")

#計算檢定統計量
chi_squared_stat = (((observed-expected)**2)/expected).sum()
print(chi_squared_stat)

#計算卡方檢定的critical value(95%信心水準下)
crit = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 2)   # df = number of variable categories - 1
print("Critical value:",crit)

#計算pvalue
p_value = 1 - stats.chi2.cdf(x=chi_squared_stat,  # Find the p-value
                             df=2)
print("P value:",p_value)

#>>col_0
count    2.62
dtype: float64
#>>Critical value: 5.991464547107979
#>>P value: [0.26982006]
#從結果可以得知檢定統計量=2.62<5.99-->接受虛無假說-->此作物後代基因比例符合1:2:1


#也可以用內建公式stats.chisquare()，直接計算檢定統計量與p-value
(statistic,pvalue)=stats.chisquare(f_obs= observed,   # Array of observed counts
                                   f_exp= expected)   # Array of expected counts
print(statistic,pvalue)
#>>[2.62] [0.26982006]
