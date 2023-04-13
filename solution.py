import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import pareto, cauchy, norm, ttest_ind, ks_2samp, mannwhitneyu, permutation_test # нужен новый scipy

chat_id = 278913153 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия

    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    #return ... # Ваш ответ, True или False  

    pval_tz = 0.03
    alternative = 'less'    
    #alternative='smaller'

    #stat, pval = ttest_ind(x, y, equal_var=False, alternative=alternative)
    zstat, pvalue = ttest_ind(x, y, equal_var=False, alternative=alternative)
    print('zstat=', zstat)
    print('pvalue', pvalue)

    #print('{0:0.3f}'.format(pval))

    if ( pval < 0.5 + pval_tz) and ( zstat > 0 ):
      return True
    else: 
      return False

'''
# 1 балл получил

import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.proportion import proportions_ztest

chat_id = 278913153 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия

    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    #return ... # Ваш ответ, True или False  

    pval_tz = 0.03

    count = x
    #np.sum(x)
    print(count)
    nobs = y
    #np.sum(y)
    print(nobs)
    stat, pval = ztest(count, nobs, alternative='smaller')
    #print('{0:0.3f}'.format(pval))

    if pval < pval_tz:
      return True
    else:
      return False
'''
