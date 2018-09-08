from jqdatasdk import *
auth('13601209121','jkal2so43')

#stocks = list(get_all_securities(['stock']).index)

# 获取2018-08-01的龙虎榜数据
lhb=get_billboard_list(stock_list=None, end_date = '2018-09-06', count =1)

zj=get_money_flow('000001.XSHE', '2016-02-01', '2016-02-04', fields="change_pct")

ppp =get_price('000300.XSHG',start_date='2018-01-01',end_date='2018-01-10')
print(ppp)