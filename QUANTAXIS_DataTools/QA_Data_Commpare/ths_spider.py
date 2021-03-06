# coding:utf-8

import requests
import pandas as pd
import numpy as np



def get_k_data_year(code,year,if_fq):
    data_=[]


    url='http://d.10jqka.com.cn/v2/line/hs_%s/%s/%s.js'%(str(code),str(if_fq),str(year))
    for item in requests.get(url).text.split('\"')[3].split(';'):
        data_.append(item.split(','))
    return pd.DataFrame(data_,index=list(np.asarray(data_).T[0]),columns=['date','open','high','low','close','volume','amount','factor'])


if __name__=='__main__':
    print(get_k_data_year('000001','2016','01'))
    print(get_k_data_year(600010,2016,'01'))