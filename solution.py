import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 278913153 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия

    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    #return ... # Ваш ответ, True или False  

    pval_tz = 0.03

    count = np.sum(x)
    nobs = np.sum(y)
    stat, pval = proportions_ztest(count, nobs, alternative='smaller')
    #print('{0:0.3f}'.format(pval))

    if pval <= pval_tz:
      return True
    else:
      return False
