from scipy import stats
import numpy as np

#抽樣的結果 n=20
group_bps = np.array([121, 135, 128, 135, 140, 132, 123, 145, 136, 133,
                     141, 118, 117, 126, 130, 115, 146, 119, 126, 138])
sample_size=len(group_bps)
mean=np.mean(group_bps)  #計算平均值
standard_error=stats.sem(group_bps)  #計算standard error of the mean(標準誤)
(statistic, pvalue) = stats.ttest_1samp(group_bps, 120)  #t 的檢定值/p-value，如上公式所述

#stats.ttest.1_samp():是雙尾檢定，會回傳statistic(檢定值)與p-value

print("Standard_error_of_the_mean is",standard_error)
print("mean is",mean)
print("t statistic is: ", statistic)
print("pvalue is: ", pvalue)

