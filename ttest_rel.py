#paired t-test
import numpy as np
from scipy import stats

#某種新上市高血壓藥物，進行臨床試驗，今天隨機取出10位50-60歲的高血壓患者，開始服藥，並記錄服藥前後的血壓值
before = np.array([148, 150, 146, 156, 151, 160, 153, 145, 152, 144])
after = np.array([140, 134, 132, 150, 142, 141, 151, 140, 148, 136])

(statistic, pvalue)=stats.ttest_rel(before, after)

print("t statistic is:",statistic)
print("pvalue is:",pvalue)

#>>t statistic is: 5.20685252381914
#>>pvalue is: 0.0005589171904489799
#我們可以解釋，在α=0.05信心水準下，因為p值<0.05(或是t檢定值落在接受域)，因此可以拒絕假設檢定=>代表此藥物對於高血壓有療效
