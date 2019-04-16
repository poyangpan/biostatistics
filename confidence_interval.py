#計算信賴區間
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
import math

#建立一個常態母群體 平均數為5.5 標準差為1
population= stats.norm.rvs(size=100000,loc = 5.5,scale=1)

#建立抽樣
np.random.seed(10)
sample_size = 16

#從母群體中抽出100個樣本
sample = np.random.choice(a= population, size = sample_size)

#計算樣本平均數
sample_mean=sample.mean()
print("sample mean=",sample_mean)

#計算95%信心水準下的Z值
z_critical = stats.norm.ppf(q = 0.975)
print("z-critical value:",z_critical) 

#計算誤差範圍(margin of error)
margin_of_error = z_critical * (1/math.sqrt(sample_size))
confidence_interval = (sample_mean - margin_of_error,
                       sample_mean + margin_of_error)  
print("95%_confidence interval:",confidence_interval)

#所得結果
#sample mean= 5.426405361401013
#z-critical value: 1.959963984540054
#95%_confidence interval: (4.936414365266, 5.916396357536026)
#從抽樣的結果來看，我們所獲得的信賴區間為(4.94,5.92)，其代表的意義是在95%信心水準下，有95%的信心相信此區間會包含母群體平均數
