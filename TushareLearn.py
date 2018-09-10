import tushare as ts


#获取全部股票代码
stock = ts.get_stock_basics()

#统计换手率
def turnOverCheck(turnover):
    sum =0
    for t in turnover:
        sum=sum+t

    return sum

#取前十个，主要是测试
code  = stock.index[:10]
outstanding = stock['outstanding'][:10]*100000000
#print(outstanding)
i=0;

#统计换手率
def turnovercheck2(turnover,count,date):
    k =1
    m =0

    sum=0
    for t in turnover:
        sum = sum+t
        k = k+1
        m = m+1
        #print(sum)
        if (k==count):
            k=1
            if (sum>10):
                print (date[m],sum)
            sum=0



for eachCode in code:
    his = ts.get_hist_data(eachCode)
   # print(his)
    turnover = his['volume'] / outstanding[i]
    turnover = turnover * 100 * 100
    print(eachCode)
    turnovercheck2(turnover,3,his.index)

    i=i+1



'''
for eachCode in code:
    #print(type(eachCode))
    # 获取历史数据
    his=ts.get_hist_data(eachCode,start='2018-09-06',end='2018-09-10')
    #print('--------------volume------------')
    ##print(his['volume'])
    #print('--------------volume end------------')
    turnover = his['volume']/outstanding[i]
    turnover = turnover*100*100
    #print('--------------turn over------------')
    #print(turnover)
    #print('--------------turn end------------')

    tosum=turnOverCheck(turnover)
    #print(eachCode, tosum)
    if tosum>10:
        print (eachCode,tosum)

    i = i+1
print("This is end of program")
'''

'''

#his=ts.get_hist_data('600848',index=False) #一次性获取全部日k线数据

data=ts.get_k_data('300032')

#his=ts.get_h_data('600848', index=False,start='2016-10-01', end='2016-10-31')

#print(data.info())

#print(data[:5])

#print(ts.__verson__)
#stock = stock.values
print(stock.columns.values.tolist())
#print(stock['name'])
for code in stock.index:
  print(code)

'''