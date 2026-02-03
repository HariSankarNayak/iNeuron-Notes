# Linear Regression
```python
# import Require librarires
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x, y, test_size= 0.33, random_state= 10)

from sklearn.preprocessing import StandardScaler
scaler= StandardScaler()

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

import statsmodels.formula.api as smf
lm= smf.ols(formula= "", data= dataset).fit()
lm.summary()
```
# Ridge Regression

```python
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
ridge_regressor= Ridge()
ridge_regressor
Ridge()
parameters= {'alpha':[1,2,5,10,20,30,40,50,60,70,80,90]}

ridgecv= GridSearchCV(ridge_regressor, parameters, scoring= 'neg_mean_squared_error', cv= 5)
ridgecv.fit(x_train, y_train)
ridgecv.best_params_
```

# Lasso Regression

```python
from sklearn.linear_model import Lasso
lasso= Lasso()
lasso
Lasso()
parameters= {'alpha':[1,2,5,10,20,30,40,50,60,70,80,90]}

lassocv= GridSearchCV(lasso, parameters, scoring= 'neg_mean_squared_error', cv= 5)
lassocv.fit(x_train, y_train)

# print(lassocv.best_params_)
lassocv.best_score_
```

# Elastic-Net Regression

```python
from sklearn.linear_model import ElasticNet
elastic_net_reg= ElasticNet()
elastic_net_reg
ElasticNet()
## Passing independent and dependent training dataset to the model
elastic_net_reg.fit(x_train, y_train)
ElasticNet()
parameters= {'alpha':[1,2,5,10,20,30,40,50,60,70,80,90]}
elastic_netcv= GridSearchCV(lasso, parameters, scoring= 'neg_mean_squared_error', cv= 5)
elastic_netcv.fit(x_train, y_train)

# print(elastic_netcv.best_params_)
elastic_netcv.best_score_
```
