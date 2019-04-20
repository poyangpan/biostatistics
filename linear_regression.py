#線性迴歸
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats

#讀取csv檔案 *改成自己檔案所在路徑
score=pd.read_csv('score.csv')

from sklearn import linear_model
# Initialize model
regression_model = linear_model.LinearRegression()

# Train the model using the score data
regression_model.fit(X = pd.DataFrame(score['before']), 
                     y = score['after'])

**X必須為二維陣列，因此我們用pdDataFrame把array轉換為二維(25,)—>(25,1)

# Check trained model y-intercept
print('intercept:',regression_model.intercept_)

# Check trained model coefficients  ~slope
print('slope:',regression_model.coef_[0])

>>intercept: 8.908026256899888
>>slope: 0.8059823959421156

r_squared=regression_model.score(X = pd.DataFrame(score['before']), 
                     y = score['after'])
print('r_squared:',r_squared)
>>0.719722296541699

#1.得到配適迴歸的Y^
score_prediction = regression_model.predict(X = pd.DataFrame(score["before"]))
**為np array (25,)
#2.算殘差 Actual - prediction = residuals = (Y-Y^)
residuals = score["after"] - score_prediction
residuals.describe()
#3.算誤差平方和 SSE=error sum of squares
SSResiduals = (residuals**2).sum()
#4.算總平方和 SST=total sum of squares =(Yi-Ybar)
SSTotal = ((score["after"] - score["after"].mean())**2).sum()
# R-squared=r^2=SSR/SST=1-SSE/SST  =>linear model!!
r_squared_func=1 - (SSResiduals/SSTotal)
print(r_squared_func)

#繪製散布圖
x=score['before']  —>pd.Series (25,)
y=score['after']
plt.scatter(x,y,color='black',label="score")

# Plot regression line
plt.plot(x,   # Explanitory variable
         score_prediction,  # Predicted values
         color="blue",
         label="regression line")
#標示線條類型
plt.legend(loc='lower right')
