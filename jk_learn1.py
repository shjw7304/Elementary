from jqdatasdk import *
from jqdatasdk import finance
from  sqlalchemy.orm.query import *

auth('13601209121','jkal2so43')
'''
q=query(finance.STK_SHAREHOLDER_FLOATING_TOP10).filter(finance.STK_SHAREHOLDER_FLOATING_TOP10.code=='600221.XSHG',finance.STK_SHAREHOLDER_FLOATING_TOP10.pub_date>'2018-01-01').limit(10)
df=finance.run_query(q)
print(df[['shareholder_name','share_ratio']])
'''

#将所有股票列表转换成数组
#stocks = get_all_securities('stock')

stock = get_security_info('000001.XSHE')
print(stock)

