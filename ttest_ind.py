# tw sample t test
from scipy import stats
import numpy as np

#欲檢定兩獨立群體抽樣的血壓收縮壓值平均(mean SBP)是否相同?
group1_bps = [124, 122, 138, 112, 146, 140, 135, 120, 132, 135,
                     121, 112, 140, 128, 130, 129, 130, 125, 120, 122]

group2_bps = [128, 125, 122, 110, 126, 130, 133, 111, 121, 120,
                       126, 124, 128, 132, 114, 115, 129, 124, 120, 125]

#stats.ttest_ind() : 計算兩獨立樣本的t檢定統計值，在假設兩母體變異數相同情況下
(statistic, pvalue) = stats.ttest_ind(group1_bps, group2_bps)

print( "t statistic is: ", statistic)
print ("pvalue is: ", pvalue)

#獲得的結果：
#t statistic is:  1.9315415052188656
#pvalue is:  0.0608992656657496

#我們可以解釋，在α=0.05信心水準下，因為p值>0.05(或者說t檢定值落在接受域)，因此可以接受假設檢定=>代表此兩群體的收縮壓平均值相相同
