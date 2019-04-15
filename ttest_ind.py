# twp sample t test
from scipy import stats
import numpy as np

group1_bps = [124, 122, 138, 112, 146, 140, 135, 120, 132, 135,
                     121, 112, 140, 128, 130, 129, 130, 125, 120, 122]

group2_bps = [128, 125, 122, 110, 126, 130, 133, 111, 121, 120,
                       126, 124, 128, 132, 114, 115, 129, 124, 120, 125]

(statistic, pvalue) = stats.ttest_ind(group1_bps, group2_bps)

print( "t statistic is: ", statistic)
print ("pvalue is: ", pvalue)
