from scipy import stats
import numpy as np

#假設隨機抽樣的結果，樣本數n=20，樣本血壓值
group_bps = np.array([121, 135, 128, 135, 140, 132, 123, 145, 136, 133,
                     141, 118, 117, 126, 130, 115, 146, 119, 126, 138])
sample_size=len(group_bps)
mean=np.mean(group_bps)  #計算平均值
standard_error=stats.sem(group_bps)  #計算standard error of the mean(標準誤)

#假設檢定，H0:樣本的血壓等於120
(statistic, pvalue) = stats.ttest_1samp(group_bps, 120)  #t 的檢定值/p-value，如上公式所述

#stats.ttest.1_samp():是雙尾檢定，會回傳statistic(檢定值)與p-value
print("Standard_error_of_the_mean is",standard_error)
print("mean is",mean)
print("t statistic is: ", statistic)
print("pvalue is: ", pvalue)

#計算t-critical value，在95%信心水準下，df(自由度)=n-1
t_critical = stats.t.ppf(q = 0.975, df=19)  
print("t-critical value:")   
print(t_critical)                        

#計算樣本標準差
stdev = group_bps.std(ddof=1)    # Get the sample standard deviation
print(stdev)
#計算標準誤
sigma = stdev/math.sqrt(sample_size)  # Standard deviation estimate
margin_of_error = t_critical * sigma
#計算信賴區間
confidence_interval = (mean - margin_of_error,
                       mean + margin_of_error)  
print("Confidence interval:")
print(confidence_interval)
